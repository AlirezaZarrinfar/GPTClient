from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from api.models import Chat
from api.utils import send_code_to_api

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("id","send","response","user_id")
        extra_kwargs = {
            "response":{"read_only":True},
            "_user_id":{"read_only":True}
        }
    
    def create(self, validated_data):
        request = self.context.get("request")
        ch = Chat(**validated_data)
        ch.user = request.user
        response = send_code_to_api(validated_data["send"])
        ch.response = response
        ch.save()
        return ch


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "password":{"write_only":True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type":"password"},trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(request=self.context.get("request"),username=username, password=password)
        if not user:
            msg = "Authentication credentials were not provided."
            raise serializers.ValidationError(msg, code="authentication")
        attrs["user"] = user
        return attrs