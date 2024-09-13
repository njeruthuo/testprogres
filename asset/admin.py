from .models import AssetRegister
from django.contrib import admin

# Register your models here.
from .models import Asset, Client, AssetRegister

from django.contrib import admin
from .models import Asset


class AssetAdmin(admin.ModelAdmin):
    list_display = ('vehicle_reg_no', 'make_and_model',
                    'asset_status', 'tracking_status')
    # Adds a filter by asset_status in the sidebar
    list_filter = ('asset_status',)


# Register the model and the custom admin class
admin.site.register(Asset, AssetAdmin)


class AssetRegisterAdmin(admin.ModelAdmin):
    list_display = (
        'asset_vehicle_reg_no',  # Show asset's vehicle registration number
        'client__first_name',           # Show client's name
        'client__last_name',
        'loan__loan_batch_number',             # Show loan information
        'remedial__tracking_vendor',         # Show remedial information
        'main_status',           # Show the computed main status
        'backup_status',         # Show the computed backup status
        'location',              # Show the location
    )

    def asset_vehicle_reg_no(self, obj):
        return obj.asset.vehicle_reg_no
    asset_vehicle_reg_no.short_description = 'Vehicle Reg No'

    def client_name(self, obj):
        return obj.client.name if obj.client else 'No Client'
    client_name.short_description = 'Client'

    def loan_info(self, obj):
        return obj.loan.loan_number if obj.loan else 'No Loan'
    loan_info.short_description = 'Loan'

    def remedial_info(self, obj):
        return obj.remedial.description if obj.remedial else 'No Remedial'
    remedial_info.short_description = 'Remedial'


admin.site.register(AssetRegister, AssetRegisterAdmin)


admin.site.register(Client)
