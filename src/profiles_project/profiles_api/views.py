from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from . import serializers

# Create your views here.


class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer()


    def get(self, request, format=None):
        """Returns a list of APIView FEATURES"""

        an_apiview=[
        'uses http methods as function(get, post, patch, put, delete)',
        'it is similiar to traditional django view',
        'gives you the most control over your logic'
        'it is mapped manually to urls'

        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})


        def post(self, request):
             """create a hello message with our name """
        serializer = serializers.HelloSerializer(data = request.data())

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})

        else:

            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def put(self, request, pk=None):
            """Handles updating an object"""

            return Response({'method': 'put'})

        def patch(self, request, pk=None):
            """ patch request, only updates fields provided in the request"""

            return Response({'method': 'patch'})

        def delete(self, request, pk=None):
            """deletes an object"""

            return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Tets API ViewSet"""

    def list(self, request):
        """return a hello message"""

        a_viewset=[

        'uses actions(list, create, retrieve, update, partial_update, destroy)',
        'Automatically maps to URLs using routers',
        'Provides more functionality with less code'
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})
