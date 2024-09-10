from rest_framework import status, generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import ClientSerializer
from .models import Client


class ClientAPIView(generics.GenericAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk:
            client = get_object_or_404(Client, pk=pk)
            serializer = self.serializer_class(client)
            return Response(serializer.data, status=status.HTTP_200_OK)

        clients = Client.objects.all()
        serializer = self.serializer_class(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


client_create_list = ClientAPIView.as_view()
