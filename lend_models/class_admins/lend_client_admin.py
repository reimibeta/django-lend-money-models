# lend admin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter

from lend_models.class_models.lend_client import LendClientSet, LendClient


class LendClientSetAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_per_page = 25
    search_fields = ['name', ]


admin.site.register(LendClientSet, LendClientSetAdmin)


class LendClientAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'created_date',
        'updated_date',
        'is_active',
    ]
    list_display_links = [
        'client',
    ]
    list_per_page = 25

    list_filter = (
        # for ordinary fields
        ('created_date', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('lend', RelatedDropdownFilter),
        ('client', RelatedDropdownFilter),
    )
    list_editable = [
        'is_active'
    ]

    # search_fields = []

    inlines = []


admin.site.register(LendClient, LendClientAdmin)
