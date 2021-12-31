from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from .models import User


class UserView(APIView):
    # GET /api/user/{pk}
    def get(self, request,  **kwargs):
        if kwargs.get('pk') is None:
            queryset = User.objects.all()
            serializer_class = UserSerializer(queryset, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            pk = kwargs.get('pk')
            user_serializer = UserSerializer(
                User.objects.get(id=pk))  # id에 해당하는 User의 정보를 불러온다
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    # POST /api/user/
    def post(self, request):
        # Request의 data를 UserSerializer로 변환
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()  # UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            # client에게 JSON response 전달
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT /api/user/{pk}
    def put(self, request, **kwargs):
        if kwargs.get('pk') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            pk = kwargs.get('pk')
            user_object = User.objects.get(id=pk)

            update_user_serializer = UserSerializer(
                user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    # DELETE /api/user/{pk}
    def delete(self, request, **kwargs):
        if kwargs.get('pk') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            pk = kwargs.get('pk')
            user_object = User.objects.get(id=pk)
            user_object.delete()
            return Response("delete ok", status=status.HTTP_200_OK)
