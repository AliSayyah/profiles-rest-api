from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """returns a list of apiview features"""
        an_apiview = [
            'uses HTTP methods as function (get, post, path, put, delete)',
             'is similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]
        return Response({'massage':'hello!','an_apiview': an_apiview})