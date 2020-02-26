from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, reponse, format=None):
        an_apiview = [
            'first_item',
            'second_item',
            'third_item',
            'fourth_item',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
