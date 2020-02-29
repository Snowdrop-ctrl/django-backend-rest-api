from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

from profile_app import serializers


class helloview(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.HelloSerializers

    def get(self,request,formate=None):
        view = [
        'hello',
        'nitesh',
        'nothing'
        ]

        return Response({'massage':'dddddd','view':view})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            massage = f'hello {name}'
            return Response({'massage':massage})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        return Response('opration {put}')

    def patch(self, request, pk=None):
        return Response('opration {patch}')

    def delete(self, request, pk=None):
        return Response('opration {delete}')
