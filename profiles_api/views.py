from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses various methods as functions: get, post, patch, put, delete.', 
            'Is simialr to the traditional django view', 
            'Hello world!',
            'Most control over the app logic'
        ]

        return Response({'message':'Hello Again!', 'an_apiview':an_apiview})