from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class SpellAPIView(APIView):
     """Test Api View"""
     def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'spells', 'an_apiview': an_apiview})