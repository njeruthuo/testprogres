from django.contrib import admin
from .models import Loan, LoanRequirement, Bank

admin.site.register(Bank)


class LoanRequirementInline(admin.TabularInline):
    model = LoanRequirement
    extra = 1
    can_delete = True


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['loan_batch_number', 'loan_status',
                    'loan_start_date', 'loan_end_date']
    inlines = [LoanRequirementInline]


@admin.register(LoanRequirement)
class LoanRequirementAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_file', 'pin_file', 'offer_letter', 'tracking_certificate',
                    'tracking_invoice', 'tracking_vendor', 'insurance_certificate']
