from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import RemedialSerializer
from .models import Remedial


class RemedialAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk:
            remedial = get_object_or_404(Remedial, pk=pk)
            serializer = RemedialSerializer(remedial)
            return Response(serializer.data, status=status.HTTP_200_OK)

        remedial_list = Remedial.objects.all()
        serializer = RemedialSerializer(remedial_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RemedialSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


remedial_list_create = RemedialAPIView.as_view()
