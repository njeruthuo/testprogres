from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import AssetSerializer
from .models import Asset


class AssetAPIView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()

    def get(self, request, *args, **kwargs):
        # Fetch all Asset objects
        assets = self.get_queryset()

        # Serialize the assets
        serializer = self.serializer_class(assets, many=True)

        # Return serialized data with status code 200
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


asset_api_view = AssetAPIView.as_view()
