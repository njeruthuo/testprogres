from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Loan, LoanRequirement, Bank
from .serializers import LoanSerializer, LoanRequirementSerializer, BankSerializer


class BankAPIView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoanAPIView(APIView):
    def get(self, request, pk=None):
        """Get a list of all loans or a single loan by its primary key (pk)."""
        if pk:
            loan = get_object_or_404(Loan, pk=pk)
            serializer = LoanSerializer(loan)
        else:
            # Retrieve all loans
            loans = Loan.objects.all()
            serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new loan and its requirements."""
        # Only pass request.data for loan fields
        loan_serializer = LoanSerializer(data=request.data)

        if loan_serializer.is_valid():
            loan = loan_serializer.save()

            # Handle file uploads and loan requirements
            files = request.FILES  # Collect all uploaded files

            loan_requirements_data = {
                'loan': loan.id,
                'id_file': files.get('loan_requirements.id_file'),
                'pin_file': files.get('loan_requirements.pin_file'),
                'offer_letter': files.get('loan_requirements.offer_letter'),
                'tracking_certificate': files.get('loan_requirements.tracking_certificate'),
                'tracking_invoice': files.get('loan_requirements.tracking_invoice'),
                'tracking_vendor': files.get('loan_requirements.tracking_vendor'),
                'insurance_certificate': files.get('loan_requirements.insurance_certificate'),
            }

            # Save loan requirements associated with the loan
            requirement_serializer = LoanRequirementSerializer(
                data=loan_requirements_data
            )

            if requirement_serializer.is_valid():
                requirement_serializer.save()
            else:
                # Rollback if the loan requirements are invalid
                loan.delete()
                return Response(requirement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(loan_serializer.data, status=status.HTTP_201_CREATED)

        return Response(loan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
