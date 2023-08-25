from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import AppUser
from .validations import (validate_changed_password, validate_name,
			  			 validate_changed_name, validate_email,
						 validate_password, validate_surname
						 )
from django.contrib.auth import authenticate, get_user_model

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True)
	name = serializers.CharField(required=True)
	surname = serializers.CharField(required=True)
	password = serializers.CharField(required=True, write_only=True)
	class Meta:
		model = UserModel
		fields = ('user_id', 'email', 'name', 'surname', 'password')
		
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
		user_obj.name = clean_data['name']
		user_obj.surname = clean_data['surname']
		user_obj.save()
		return user_obj

class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField(write_only=True, required=True)
	password = serializers.CharField(write_only=True, required=True)
	def check_user(self, clean_data):
		user = authenticate(username=clean_data['email'], password=clean_data['password'])
		if not user:
			raise TypeError('user not found')
		return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('email', 'name', 'surname', "user_id")

class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_changed_password])
    repeat_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AppUser
        fields = ('old_password', 'new_password', 'repeat_password')

    def validate(self, attrs):
        if attrs['new_password'] != attrs['repeat_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('name', 'surname')