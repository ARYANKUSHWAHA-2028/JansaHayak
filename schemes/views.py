from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Scheme


def scheme_detail(request, pk):

    scheme = get_object_or_404(Scheme, pk=pk)

    return render(
        request,
        'schemes/scheme_detail.html',
        {
            'scheme': scheme
        }
    )


def scheme_list(request):

    search_query = request.GET.get('search', '')

    schemes = Scheme.objects.all()

    if search_query:

        schemes = schemes.filter(
            name__icontains=search_query
        )

    paginator = Paginator(
        schemes,
        6
    )

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'schemes/scheme_list.html',
        {
            'schemes': page_obj,
            'search_query': search_query
        }
    )
    