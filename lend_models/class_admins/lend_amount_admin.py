# lend admin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter

from lends.class_models.lend_amount import LendAmount


class LendAmountAdmin(admin.ModelAdmin):
    list_display = [
        'lend',
        'money',
        'return_date',
        'is_return'
    ]
    list_display_links = [
        'lend',
        'money'
    ]
    list_per_page = 25

    list_filter = (
        # for ordinary fields
        ('return_date', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('lend', RelatedDropdownFilter),
        # ('client', RelatedDropdownFilter),
    )
    list_editable = [
        # 'return_date',
        # 'is_return',
    ]
    # search_fields = []
    # exclude = ['is_return', ]
    inlines = []

    def money(self, obj):
        return "{} {}".format(obj.amount, obj.account.currency.currency)


admin.site.register(LendAmount, LendAmountAdmin)


class LendAmountInlineAdmin(admin.TabularInline):
    model = LendAmount
    extra = 0
    # exclude = ['re', ]
