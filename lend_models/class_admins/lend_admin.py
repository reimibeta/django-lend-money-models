# lend admin
from django.contrib import admin
from django.db.models import Sum
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter

from lend_models.class_admins.lend_amount_admin import LendAmountInlineAdmin
from lend_models.class_models.lend import Lend


class LendAdmin(admin.ModelAdmin):
    list_display = [
        # 'wallet',
        'client',
        # 'amount',
        'lend_date',
    ]
    list_display_links = [
        # 'wallet',
        'client'
    ]
    list_per_page = 25

    list_filter = (
        # for ordinary fields
        ('lend_date', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('wallet', RelatedDropdownFilter),
        ('client', RelatedDropdownFilter),
    )
    # list_editable = []
    search_fields = [
        # 'wallet',
    ]

    inlines = [
        LendAmountInlineAdmin,
    ]

    # def amount(self, obj):
    #     total_amount = LendAmount.objects.filter(lend=obj.id).aggregate(Sum('amount'))['amount__sum']
    #     return "{} {}".format(
    #         total_amount,
    #         obj.currency.currency if obj.currency.currency is not None else 'not provided'
    #     )


admin.site.register(Lend, LendAdmin)
