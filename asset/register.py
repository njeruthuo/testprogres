from .models import Loan, AssetRegister, Asset
from .serializers import AssetRegisterSerializer
from .serializers import AssetSerializer, AssetRegisterSerializer

from clients.serializers import ClientSerializer
from remedial.serializers import RemedialSerializer
from loan.serializers import LoanRequirementSerializer, LoanSerializer, Loan, LoanRequirement

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import transaction
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# class AssetRegisterAPIView(APIView):

#     @transaction.atomic  # Ensure atomicity in case of failure
#     def post(self, request):
#         errors = {}

#         # print(request.data)

#         # Example of retrieving values from the QueryDict
#         # loan_id = request.POST.get('loan[loan_id]')
#         # deposit_amount = request.POST.get('loan[deposit_amount]')
#         # loan_amount = request.POST.get('loan[loan_amount]')
#         # loan_status = request.POST.get('loan[loan_status]')
#         # loan_start_date = request.POST.get('loan[loan_start_date]')
#         # loan_end_date = request.POST.get('loan[loan_end_date]')
#         # loan_period = request.POST.get('loan[loan_period]')

#         loan_data = {
#             'loan_id': request.POST.get('loan[loan_id]'),
#             'deposit_amount': request.POST.get('loan[deposit_amount]'),
#             'loan_amount': request.POST.get('loan[loan_amount]'),
#             'loan_status': request.POST.get('loan[loan_status]'),
#             'loan_start_date': request.POST.get('loan[loan_start_date]'),
#             'loan_end_date': request.POST.get('loan[loan_end_date]'),
#             'loan_period': request.POST.get('loan[loan_period]'),
#         }

#         # print(loan_data)

#         # Asset fields

#         asset = {
#             'vehicle_reg_no': request.POST.get('asset[vehicle_reg_no]'),
#             'make_and_model': request.POST.get('asset[make_and_model]'),
#             'asset_value': request.POST.get('asset[asset_value]'),
#             'purchase_price': request.POST.get('asset[purchase_price]'),
#             'chasis': request.POST.get('asset[chasis]'),
#             'dealer': request.POST.get('asset[dealer]'),
#             'tracking_status': request.POST.get('asset[tracking_status]'),
#             'asset_type': request.POST.get('asset[asset_type]'),
#             'color': request.POST.get('asset[color]'),
#             'insurance_value': request.POST.get('asset[insurance_value]'),
#             'engine': request.POST.get('asset[engine]'),
#             'asset_status': request.POST.get('asset[asset_status]')},

#         # asset = dict(asset)

#         # print(asset[0])

#         # Client fields
#         client = {
#             'first_name': request.POST.get('client[first_name]'),
#             'last_name': request.POST.get('client[last_name]'),
#             'company_name': request.POST.get('client[company_name]'),
#             'id_number': request.POST.get('client[id_number]'),
#             'mobile_number': request.POST.get('client[mobile_number]'),
#             'email_address': request.POST.get('client[email_address]'),
#             'PIN_number': request.POST.get('client[PIN_number]'),
#         }

#         # print(client)

#         # Remedial fields

#         remedial = {
#             'tracking_vendor': request.POST.get('remedial[tracking_vendor]'),
#             'repossession_vendor': request.POST.get('remedial[repossession_vendor]'),
#             'date_of_repossession': request.POST.get(
#                 'remedial[date_of_repossession]'),
#             'history_log': request.POST.get('remedial[history_log]'),
#         }

#         # print(remedial)
#         # Loan Requirements (handling files)
#         loan_requirements = {

#             'id_file': request.FILES.get('loan[loan_requirements][id_file]'),
#             'pin_file': request.FILES.get('loan[loan_requirements][pin_file]'),
#             'offer_letter': request.FILES.get(
#                 'loan[loan_requirements][offer_letter]'),
#             'tracking_certificate': request.FILES.get(
#                 'loan[loan_requirements][tracking_certificate]'),
#             'tracking_invoice': request.FILES.get(
#                 'loan[loan_requirements][tracking_invoice]'),
#             'tracking_vendor': request.FILES.get(
#                 'loan[loan_requirements][tracking_vendor]'),
#             'insurance_certificate': request.FILES.get(
#                 'loan[loan_requirements][insurance_certificate]'),
#         }

#         # loan_data = request.data.get('loan')
#         loan_serializer = LoanSerializer(data=loan_data)
#         loan = None

#         if loan_serializer.is_valid():
#             loan = loan_serializer.save()
#         else:
#             errors['loan'] = loan_serializer.errors

#         # Handle Loan Requirements creation if Loan is valid
#         if loan:
#             # loan_requirements_data = loan_data.get('loan_requirements', {})
#             loan_requirements_data = loan_requirements
#             # Assign loan ID to requirements
#             loan_requirements_data['loan'] = loan.id
#             loan_requirements_serializer = LoanRequirementSerializer(
#                 data=loan_requirements_data)

#             if loan_requirements_serializer.is_valid():
#                 loan_requirements_serializer.save()
#             else:
#                 errors['loan_requirements'] = loan_requirements_serializer.errors
#         else:
#             errors['loan_requirements'] = "Loan must be valid to add requirements."

#         # Handle Client creation
#         # client_data = request.data.get('client')
#         client_data = client
#         client_serializer = ClientSerializer(data=client_data)

#         if client_serializer.is_valid():
#             client_serializer.save()
#         else:
#             errors['client'] = client_serializer.errors

#         # Handle Remedial creation
#         # remedial_data = request.data.get('remedial')
#         remedial_data = remedial
#         remedial_serializer = RemedialSerializer(data=remedial_data)

#         if remedial_serializer.is_valid():
#             remedial_serializer.save()
#         else:
#             errors['remedial'] = remedial_serializer.errors

#         # Handle Asset creation
#         # asset_data = request.data.get('asset')
#         asset_data = asset[0]
#         asset_serializer = AssetSerializer(data=asset_data)

#         if asset_serializer.is_valid():
#             asset_serializer.save()
#         else:
#             errors['asset'] = asset_serializer.errors

#         # Check if there are any errors
#         if errors:
#             # Rollback the transaction if any errors occurred
#             transaction.set_rollback(True)
#             return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

#         # If everything is successful, return a combined success response
#         return Response({
#             "loan": loan_serializer.data,
#             "loan_requirements": loan_requirements_serializer.data,
#             "client": client_serializer.data,
#             "remedial": remedial_serializer.data,
#             "asset": asset_serializer.data,
#         }, status=status.HTTP_201_CREATED)


class AssetRegisterV2(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('id')

        if pk is not None:
            asset = get_object_or_404(AssetRegister, pk=pk)
            obj_serializer = AssetRegisterSerializer(asset)
            return Response(obj_serializer.data, status=status.HTTP_200_OK)

        # Pagination parameters
        page = request.query_params.get('page', 1)
        page_size = request.query_params.get('page_size', 10)

        try:
            page_size = int(page_size)
        except ValueError:
            page_size = 10  # Default value if page_size is invalid

        assets = AssetRegister.objects.all()
        paginator = Paginator(assets, page_size)

        try:
            assets_page = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            assets_page = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            assets_page = paginator.page(paginator.num_pages)

        obj_serializer = AssetRegisterSerializer(assets_page, many=True)
        response_data = {
            'results': obj_serializer.data,
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': assets_page.number,
            'next': assets_page.has_next() and request.build_absolute_uri('?page=' + str(assets_page.next_page_number())) or None,
            'previous': assets_page.has_previous() and request.build_absolute_uri('?page=' + str(assets_page.previous_page_number())) or None
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        # Extract asset, client, remedial, and loan data
        asset = {
            'vehicle_reg_no': request.POST.get('asset[vehicle_reg_no]'),
            'make_and_model': request.POST.get('asset[make_and_model]'),
            'asset_value': request.POST.get('asset[asset_value]'),
            'purchase_price': request.POST.get('asset[purchase_price]'),
            'chasis': request.POST.get('asset[chasis]'),
            'dealer': request.POST.get('asset[dealer]'),
            'tracking_status': request.POST.get('asset[tracking_status]'),
            'asset_type': request.POST.get('asset[asset_type]'),
            'color': request.POST.get('asset[color]'),
            'insurance_value': request.POST.get('asset[insurance_value]'),
            'engine': request.POST.get('asset[engine]'),
            'asset_status': request.POST.get('asset[asset_status]')
        }

        client = {
            'first_name': request.POST.get('client[first_name]'),
            'last_name': request.POST.get('client[last_name]'),
            'company_name': request.POST.get('client[company_name]'),
            'id_number': request.POST.get('client[id_number]'),
            'mobile_number': request.POST.get('client[mobile_number]'),
            'email_address': request.POST.get('client[email_address]'),
            'PIN_number': request.POST.get('client[PIN_number]')
        }

        remedial = {
            'tracking_vendor': request.POST.get('remedial[tracking_vendor]'),
            'repossession_vendor': request.POST.get('remedial[repossession_vendor]'),
            'date_of_repossession': request.POST.get('remedial[date_of_repossession]'),
            'history_log': request.POST.get('remedial[history_log]')
        }

        # Extract loan requirements and loan data
        loan_requirements = {
            'id_file': request.FILES.get('loan[loan_requirements][id_file]'),
            'pin_file': request.FILES.get('loan[loan_requirements][pin_file]'),
            'offer_letter': request.FILES.get('loan[loan_requirements][offer_letter]'),
            'tracking_certificate': request.FILES.get('loan[loan_requirements][tracking_certificate]'),
            'tracking_invoice': request.FILES.get('loan[loan_requirements][tracking_invoice]'),
            'tracking_vendor': request.FILES.get('loan[loan_requirements][tracking_vendor]'),
            'insurance_certificate': request.FILES.get('loan[loan_requirements][insurance_certificate]')
        }

        loan_data = {
            'loan_id': request.POST.get('loan[loan_id]'),
            'deposit_amount': request.POST.get('loan[deposit_amount]'),
            'loan_amount': request.POST.get('loan[loan_amount]'),
            'loan_status': request.POST.get('loan[loan_status]'),
            'loan_start_date': request.POST.get('loan[loan_start_date]'),
            'loan_end_date': request.POST.get('loan[loan_end_date]'),
            'loan_period': request.POST.get('loan[loan_period]'),
            # Passing loan requirements in a list
            'loan_requirements': [loan_requirements]
        }

        # Combine all data
        data = {
            'loan': loan_data,
            'asset': asset,
            'client': client,
            'remedial': remedial
        }

        # Validate and save the data using the serializer
        serializer = AssetRegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        transaction.set_rollback(True)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @transaction.atomic
    # def post(self, request, *args, **kwargs):
    #     # print(request.data)

    #     # Asset fields

    #     asset = {
    #         'vehicle_reg_no': request.POST.get('asset[vehicle_reg_no]'),
    #         'make_and_model': request.POST.get('asset[make_and_model]'),
    #         'asset_value': request.POST.get('asset[asset_value]'),
    #         'purchase_price': request.POST.get('asset[purchase_price]'),
    #         'chasis': request.POST.get('asset[chasis]'),
    #         'dealer': request.POST.get('asset[dealer]'),
    #         'tracking_status': request.POST.get('asset[tracking_status]'),
    #         'asset_type': request.POST.get('asset[asset_type]'),
    #         'color': request.POST.get('asset[color]'),
    #         'insurance_value': request.POST.get('asset[insurance_value]'),
    #         'engine': request.POST.get('asset[engine]'),
    #         'asset_status': request.POST.get('asset[asset_status]')},

    #     # asset = dict(asset)

    #     # print(asset[0])

    #     # Client fields
    #     client = {
    #         'first_name': request.POST.get('client[first_name]'),
    #         'last_name': request.POST.get('client[last_name]'),
    #         'company_name': request.POST.get('client[company_name]'),
    #         'id_number': request.POST.get('client[id_number]'),
    #         'mobile_number': request.POST.get('client[mobile_number]'),
    #         'email_address': request.POST.get('client[email_address]'),
    #         'PIN_number': request.POST.get('client[PIN_number]'),
    #     }

    #     # print(client)

    #     # Remedial fields

    #     remedial = {
    #         'tracking_vendor': request.POST.get('remedial[tracking_vendor]'),
    #         'repossession_vendor': request.POST.get('remedial[repossession_vendor]'),
    #         'date_of_repossession': request.POST.get(
    #             'remedial[date_of_repossession]'),
    #         'history_log': request.POST.get('remedial[history_log]'),
    #     }

    #     # print(remedial)

    #     loan_requirements = {

    #         'id_file': request.FILES.get('loan[loan_requirements][id_file]'),
    #         'pin_file': request.FILES.get('loan[loan_requirements][pin_file]'),
    #         'offer_letter': request.FILES.get(
    #             'loan[loan_requirements][offer_letter]'),
    #         'tracking_certificate': request.FILES.get(
    #             'loan[loan_requirements][tracking_certificate]'),
    #         'tracking_invoice': request.FILES.get(
    #             'loan[loan_requirements][tracking_invoice]'),
    #         'tracking_vendor': request.FILES.get(
    #             'loan[loan_requirements][tracking_vendor]'),
    #         'insurance_certificate': request.FILES.get(
    #             'loan[loan_requirements][insurance_certificate]'),
    #     }

    #     # print(loan_requirements)

    #     loan_data = {
    #         'loan_id': request.POST.get('loan[loan_id]'),
    #         'deposit_amount': request.POST.get('loan[deposit_amount]'),
    #         'loan_amount': request.POST.get('loan[loan_amount]'),
    #         'loan_status': request.POST.get('loan[loan_status]'),
    #         'loan_start_date': request.POST.get('loan[loan_start_date]'),
    #         'loan_end_date': request.POST.get('loan[loan_end_date]'),
    #         'loan_period': request.POST.get('loan[loan_period]'),
    #         'loan_requirements': [loan_requirements]
    #     }

    #     print(loan_data)

    #     data = {'loan': loan_data, 'asset': asset[0],
    #             'client': client, 'remedial': remedial, 'requirement':loan_requirements}

    #     serializer = AssetRegisterSerializer(
    #         data=data)

    #     if serializer.is_valid():
    #         data = serializer.save()
    #         return Response(data, status=status.HTTP_201_CREATED)

    #     transaction.set_rollback(True)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
