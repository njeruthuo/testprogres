# from django.db import models
# from django.core.validators import MaxLengthValidator, MinLengthValidator


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     client_id = models.IntegerField(default=-1)
#     user_name = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255, null=True, blank=True)
#     last_name = models.CharField(max_length=255, null=True, blank=True)
#     password = models.CharField(max_length=255)
#     salt = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return self.user_name


# class AssetStatus(models.Model):
#     asset_status_id = models.AutoField(primary_key=True)
#     asset_status = models.CharField(max_length=255)
#     is_deleted = models.BooleanField(default=False)
#     client_id = models.IntegerField(default=-1)

#     def __str__(self):
#         return self.asset_status


# class AssetType(models.Model):
#     asset_type_id = models.AutoField(primary_key=True)
#     asset_type = models.CharField(max_length=255)
#     is_deleted = models.BooleanField(default=False)
#     client_id = models.IntegerField(default=-1)

#     def __str__(self):
#         return self.asset_type


# class AssetOwner(models.Model):
#     asset_owner_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255, null=True, blank=True)
#     contact_details = models.CharField(max_length=255, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     id_number = models.IntegerField(default=0)
#     pin_number = models.CharField(max_length=255, null=True, blank=True)
#     is_deleted = models.BooleanField(default=False)
#     client_id = models.IntegerField(default=-1)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# class Asset(models.Model):
#     owner = models.ForeignKey('AssetOwner', on_delete=models.CASCADE)
#     type_id = models.ForeignKey(AssetType, on_delete=models.CASCADE)
#     status_id = models.ForeignKey(AssetStatus, on_delete=models.CASCADE)
#     tracking_vendor = models.ForeignKey(
#         'Vendor', on_delete=models.CASCADE, related_name='tracking_vendor')
#     repossession_vendor = models.ForeignKey(
#         'Vendor', on_delete=models.CASCADE, related_name='reposession_vendor')
#     reg_no = models.CharField(max_length=255, null=True, blank=True)
#     make_and_model = models.CharField(max_length=255, null=True, blank=True)
#     asset_value = models.DecimalField(
#         max_digits=15, decimal_places=2, default=0)
#     purchase_value = models.DecimalField(
#         max_digits=15, decimal_places=2, default=0)
#     chasis_number = models.CharField(max_length=255, null=True, blank=True)
#     engine_number = models.CharField(max_length=255, null=True, blank=True)
#     dealer_name = models.CharField(max_length=255, null=True, blank=True)
#     color = models.CharField(max_length=255, null=True, blank=True)
#     insurance_value = models.DecimalField(
#         max_digits=15, decimal_places=2, default=0)
#     latitude = models.DecimalField(
#         max_digits=9, decimal_places=6, default=-180)
#     longitude = models.DecimalField(
#         max_digits=9, decimal_places=6, default=180)
#     location_descriptor = models.CharField(
#         max_length=255, null=True, blank=True)
#     is_deleted = models.BooleanField(default=False)
#     client_id = models.ForeignKey('Client', on_delete=models.CASCADE)
#     tracking_status = models.CharField(max_length=255, null=True, blank=True)
#     status_main = models.CharField(max_length=255, null=True, blank=True)
#     status_backup = models.CharField(max_length=255, null=True, blank=True)
#     location_main = models.CharField(max_length=255, null=True, blank=True)
#     location_backup = models.CharField(max_length=255, null=True, blank=True)
#     current_loc_lat = models.DecimalField(
#         max_digits=9, decimal_places=6, default=0)
#     current_loc_lon = models.DecimalField(
#         max_digits=9, decimal_places=6, default=0)
#     tracking_expiry_date = models.DateField(null=True, blank=True)
#     installation_date = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.reg_no


# class Client(models.Model):
#     client_name = models.CharField(max_length=255, null=True, blank=True)
#     contact_person = models.CharField(max_length=255, null=True, blank=True)
#     phone_number = models.CharField(max_length=20, null=True, blank=True)
#     is_deleted = models.BooleanField(default=False)
#     up_time = models.IntegerField(default=0)

#     def __str__(self):
#         return self.client_name


# class VendorType(models.Model):
#     """
#     vendor_type_id integer NOT NULL,
#     vendor_type character varying NOT NULL,
#     is_deleted boolean DEFAULT false NOT NULL,
#     client_id integer DEFAULT '-1'::integer NOT NULL
#     """


# class Vendor(models.Model):
#     vendor_id = models.AutoField(primary_key=True)
#     vendor_type_id = models.IntegerField(default=-1)
#     vendor_name = models.CharField(max_length=255, null=True, blank=True)
#     telephone_number = models.CharField(max_length=20, null=True, blank=True)
#     address = models.CharField(max_length=255, null=True, blank=True)
#     location = models.CharField(max_length=255, null=True, blank=True)
#     contract_start_date = models.DateTimeField(null=True, blank=True)
#     contract_end_date = models.DateTimeField(null=True, blank=True)
#     regional_pressence = models.CharField(
#         max_length=255, null=True, blank=True)
#     is_deleted = models.BooleanField(default=False)
#     client_id = models.IntegerField(default=-1)

#     def __str__(self):
#         return self.vendor_name
