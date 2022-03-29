from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    # email = serializers.EmailField(required=False, default=None)
    # name = serializers.CharField(required=False, default=None)


class UserSignUpSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    name = serializers.CharField()
