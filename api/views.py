from rest_framework import views, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from api.serializers import ChatSerializer, UserSerializer, TokenSerializer
from api.models import Chat

class ChatView(views.APIView):
    serializer_class = ChatSerializer
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        operation_description="لیست تمام چت ها",
        responses={200: ChatSerializer(many=True)}
    )
    def get(self, request, format=None):
        qs = Chat.objects.filter(user=request.user)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="ایجاد یک چت جدید",
        request_body=ChatSerializer,
        responses={201: ChatSerializer}
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    @swagger_auto_schema(
        operation_description="دریافت اطلاعات کاربر",
        responses={200: UserSerializer}
    )
    def get(self, request, format=None):
        if(request.user.is_anonymous):
            return Response({"message":"Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        qs = User.objects.filter(id = request.user.id)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
            
    @swagger_auto_schema(
        operation_description="ثبت ‌نام کاربر جدید",
        request_body=UserSerializer,
        responses={201: UserSerializer}
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenView(ObtainAuthToken):
    serializer_class = TokenSerializer
    
    @swagger_auto_schema(
        operation_description="دریافت توکن احراز هویت",
        request_body=TokenSerializer,
        responses={200: TokenSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)