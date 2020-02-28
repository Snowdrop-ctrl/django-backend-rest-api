from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions




class helloview(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


    def get(self,request,formate=None):
        view = [
        'hello',
        'nitesh',
        'nothing'
        ]

        return Response({'massage':'dddddd','view':view})
