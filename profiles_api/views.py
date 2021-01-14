from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """returns a list of apiview features"""
        an_apiview = [
            'uses HTTP methods as function (get, post, path, put, delete)',
             'is similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]
        return Response({'massage':'hello!','an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                 status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def path(self, request, pk=None):
        """handles partial update of an object"""
        return Response({'method: ':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
