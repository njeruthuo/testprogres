from rest_framework import serializers
from .models import Loan, LoanRequirement, Bank


class LoanRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequirement
        fields = [
            'id', 'loan', 'id_file', 'pin_file', 'offer_letter',
            'tracking_certificate', 'tracking_invoice',
            'tracking_vendor', 'insurance_certificate'
        ]


class LoanSerializer(serializers.ModelSerializer):
    loan_requirements = LoanRequirementSerializer(many=True, required=False)

    class Meta:
        model = Loan
        fields = [
            'id', 'loan_id', 'deposit_amount', 'loan_amount',
            'loan_status', 'loan_start_date',
            'loan_end_date', 'loan_period', 'loan_requirements'
        ]

    def create(self, validated_data):
        loan_requirements_data = validated_data.pop('loan_requirements', [])
        loan = Loan.objects.create(**validated_data)

        # Create loan requirements
        for requirement_data in loan_requirements_data:
            LoanRequirement.objects.create(loan=loan, **requirement_data)

        return loan

    def update(self, instance, validated_data):
        loan_requirements_data = validated_data.pop('loan_requirements', [])
        instance.loan_id = validated_data.get('loan_id', instance.loan_id)
        instance.deposit_amount = validated_data.get(
            'deposit_amount', instance.deposit_amount)
        instance.loan_amount = validated_data.get(
            'loan_amount', instance.loan_amount)
        instance.loan_status = validated_data.get(
            'loan_status', instance.loan_status)
        instance.loan_start_date = validated_data.get(
            'loan_start_date', instance.loan_start_date)
        instance.loan_end_date = validated_data.get(
            'loan_end_date', instance.loan_end_date)
        instance.loan_period = validated_data.get(
            'loan_period', instance.loan_period)
        instance.save()

        # Update loan requirements
        existing_requirements = {
            req.id: req for req in instance.loan_requirements.all()}
        sent_requirements = []

        for requirement_data in loan_requirements_data:
            requirement_id = requirement_data.get('id')
            if requirement_id:
                # Update existing loan requirement
                requirement = existing_requirements.pop(requirement_id, None)
                if requirement:
                    for key, value in requirement_data.items():
                        setattr(requirement, key, value)
                    requirement.save()
                else:
                    # Handle case where the requirement ID is invalid or does not belong to this loan
                    raise serializers.ValidationError(
                        f"Invalid LoanRequirement ID: {requirement_id}")
            else:
                # Create new loan requirement
                LoanRequirement.objects.create(
                    loan=instance, **requirement_data)

            sent_requirements.append(requirement_id)

        # Delete loan requirements that were not sent in the update request
        for requirement_id, requirement in existing_requirements.items():
            requirement.delete()

        return instance


class BankSerializer(serializers.ModelField):
    class Meta:
        model = Bank
        fields = '__all__'
