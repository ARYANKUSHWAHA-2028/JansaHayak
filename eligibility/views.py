from django.shortcuts import render
from schemes.models import Scheme
from .models import EligibilitySearch
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def questionnaire(request):

    eligible_schemes = []

    if request.GET:

        state = request.GET.get('state', '')
        age = request.GET.get('age')
        income = request.GET.get('income')

        occupation = request.GET.get('occupation', '')

        disability = request.GET.get('disability') == 'on'
        widow = request.GET.get('widow') == 'on'

        # Save search history
        if age:
            EligibilitySearch.objects.create(
                state=state,
                age=int(age),
                occupation=occupation
            )

        schemes = Scheme.objects.all()

        for scheme in schemes:

            # State check
            if state:
                if (
                    scheme.state.lower() != 'all'
                    and scheme.state.lower() != state.lower()
                ):
                    continue

            # Age check
            if age:
                if int(age) < scheme.minimum_age:
                    continue

            # Income check
            if (
                scheme.maximum_income is not None
                and income
                and int(income) > scheme.maximum_income
            ):
                continue

            # Occupation check
            if (
                scheme.required_occupation
                and occupation != scheme.required_occupation
            ):
                continue

            # Disability check
            if scheme.disability_required and not disability:
                continue

            # Widow check
            if scheme.widow_required and not widow:
                continue

            eligible_schemes.append(scheme)

    return render(
        request,
        'eligibility/questionnaire.html',
        {
            'eligible_schemes': eligible_schemes
        }
    )
    


def download_pdf(request):

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = (
        'attachment; filename="eligibility_report.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 800, "JanSahayak Eligibility Report")

    p.setFont("Helvetica", 12)

    y = 750

    p.drawString(50, y, "Eligible Schemes:")

    y -= 30

    schemes = request.GET.getlist('schemes')

    if schemes:

        for scheme in schemes:

            p.drawString(70, y, f"• {scheme}")

            y -= 25

    else:

        p.drawString(70, y, "No schemes found.")

    p.save()

    return response