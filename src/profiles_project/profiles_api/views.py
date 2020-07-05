from django.shortcuts import render


from rest_framework.views import APIView

from rest_framework.response import Response

# Create your views here.


class HelloApiView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Returns a list of APIView FEATURES"""

        an_apiview=[
        'uses http methods as function(get, post, patch, put, delete)',
        'it is similiar to traditional django view',
        'gives you the most control over your logic'
        'it is mapped manually to urls'

        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
