from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import permissions
from profiles_api import serializers
from profiles_api import models


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, response, format=None):
        """Return 4 sample items"""
        an_apiview = [
            'first_item',
            'second_item',
            'third_item',
            'fourth_item',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with the given name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Update an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partially update an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        response_items = [
            'first_item',
            'second_item',
            'third_item'
        ]

        return Response({'message': 'Hello!', 'response_items': response_items})
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'method': 'GET'})
    
    def update(self, request, pk=None):
        return Response({'method': 'PUT'})
    
    def parital_update(self, request, pk=None):
        return Response({'method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Create and update profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
