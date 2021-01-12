from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses various methods as functions: get, post, patch, put, delete.', 
            'Is simialr to the traditional django view', 
            'Hello world!',
            'Most control over the app logic'
        ]

        return Response({'message':'Hello Again!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a message with the name provided"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handle updating objects"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of the object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Handle deleting objects"""
        return Response({'method':'DELETE'}) 


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs with Routers',
            'More func for less code'
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )

    def retrieve(self, request, pk=None):
        """Retrieve an object from the API by ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Update an object from the API by ID"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Partial update an object from the API by ID"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Removing an object from the API"""
        return Response({'http_method':'DELETE'})