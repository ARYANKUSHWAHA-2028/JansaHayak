from django.contrib import admin
from .models import Scheme


@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'state',
        'required_occupation',
        'minimum_age',
        'maximum_income',
    )

    list_filter = (
        'state',
        'required_occupation',
        'disability_required',
        'widow_required',
    )

    search_fields = (
        'name',
        'state',
    )