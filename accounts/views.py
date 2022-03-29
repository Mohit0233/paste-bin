from django.utils import timezone
from rest_framework import views
from rest_framework import views
from rest_framework.authtoken.admin import User
from rest_framework.response import Response as RestResponse

from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserLoginSerializer, UserSignUpSerializer
from paste.views import response_service


class LoginView(views.APIView):

    def post(self, request):

        ser = UserLoginSerializer(data=request.data)
        if not ser.is_valid():
            return response_service({"message": ser.errors}, True, "INVALID_DATA")

        try:
            user = User.objects.get(username=ser.validated_data['username'])
        except User.DoesNotExist:
            user = None
        if not user:
            s_ser = UserSignUpSerializer(data=request.data)
            if not s_ser.is_valid():
                return response_service({"message": s_ser.errors}, True, "INVALID_DATA")

            user = User.objects.create_user(username=s_ser.validated_data['username'], email=s_ser.validated_data['email'],
                                            password=s_ser.validated_data['password'], first_name=s_ser.validated_data['name'], last_login=timezone.now())

        token_response_dict = get_tokens_for_user(user=user)
        token_response_dict['username'] = user.username
        token_response_dict['name'] = user.first_name
        return RestResponse(data=token_response_dict, status=200)


class LogoutView(views.APIView):

    def post(self, request):
        return RestResponse(data="mom", status=200)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
