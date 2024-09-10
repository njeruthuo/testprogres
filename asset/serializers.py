from .models import Asset, AssetRegister
from rest_framework import serializers

from clients.models import Client

from remedial.serializers import RemedialSerializer, Remedial
from loan.serializers import LoanSerializer, LoanRequirement, Loan


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset

        fields = [
            'vehicle_reg_no', 'make_and_model', 'asset_value', 'purchase_price', 'chasis', 'dealer', 'tracking_status', 'asset_type', 'color',
            'insurance_value', 'engine', 'asset_status'
        ]


class AssetRegisterSerializer(serializers.ModelSerializer):

    loan = LoanSerializer()
    asset = AssetSerializer()
    client = ClientSerializer()
    remedial = RemedialSerializer()

    main_status = serializers.SerializerMethodField(read_only=True)
    backup_status = serializers.SerializerMethodField(read_only=True)
    location = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AssetRegister
        fields = '__all__'

    def get_main_status(self, obj):
        if not hasattr(obj, 'id'):
            return None

        if not isinstance(obj, AssetRegister):
            return None

        return obj.main_status

    def get_backup_status(self, obj):
        if not hasattr(obj, 'id'):
            return None

        if not isinstance(obj, AssetRegister):
            return None

        return obj.backup_status

    def get_location(self, obj):
        if not hasattr(obj, 'id'):
            return None

        if not isinstance(obj, AssetRegister):
            return None

        return obj.location

    def create(self, validated_data):
        # Pop related data
        loan_data = validated_data.pop('loan')
        asset_data = validated_data.pop('asset')
        client_data = validated_data.pop('client')
        remedial_data = validated_data.pop('remedial')
        loan_requirements_data = loan_data.pop('loan_requirements', [])

        # Create asset, client, and remedial instances
        asset = Asset.objects.create(**asset_data)
        client = Client.objects.create(**client_data)
        remedial = Remedial.objects.create(**remedial_data)

        # Create loan instance
        loan = Loan.objects.create(**loan_data)

        # Create loan requirements and associate with the loan
        for requirement_data in loan_requirements_data:
            LoanRequirement.objects.create(loan=loan, **requirement_data)

        # Finally, create and return the AssetRegister instance
        asset_register = AssetRegister.objects.create(
            loan=loan,
            asset=asset,
            client=client,
            remedial=remedial,
            **validated_data
        )

        return asset_register
