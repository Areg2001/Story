from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, ChangePasswordSerializer,\
	UserDataSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
from rest_framework.permissions import IsAuthenticated
from .models import AppUser
from rest_framework import generics


class UserRegister(generics.CreateAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = UserRegisterSerializer
	
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(generics.CreateAPIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	serializer_class=UserLoginSerializer

	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data, status=status.HTTP_200_OK)

class ChangeUserDataView(generics.RetrieveUpdateAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	serializer_class = UserDataSerializer
	
	def get_queryset(self):
		user = self.request.user
		return AppUser.objects.filter(user_id=user.user_id)

class ChangePassword(generics.UpdateAPIView):
    queryset = AppUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

