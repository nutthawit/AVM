from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import DmSerializer


class DmViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response({'message': 'Hello, World!'})

    def create(self, request):
        serializer = DmSerializer(data=request.data)
        if serializer.is_valid():
            # run Parser
            return Response({f'message: {serializer.data}'},
                            status=status.HTTP_201_CREATED)
        return Response({f'message: {serializer.errors}'})
