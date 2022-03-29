from rest_framework import views, permissions
from rest_framework.response import Response as RestResponse

# update paste
from paste.models import Paste
from paste.serializers import PasteSerializer
from paste.services import view_service


# Create your views here.
# authorize the logged user
# addPaste
# remove Scan on expiry cron


class PasteView(views.APIView):
    # authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        post_serialized_data = PasteSerializer(data=request.data)
        if not post_serialized_data.is_valid():
            return response_service({"message": post_serialized_data.errors}, True, "INVALID_DATA")

        paste_object = view_service.add_paste(title=post_serialized_data.validated_data['title'],
                                              text_data=post_serialized_data.validated_data['textData'],
                                              user_id=request.user.id,
                                              formatter=post_serialized_data.validated_data['formatter'],
                                              visibility=post_serialized_data.validated_data['visibility'],
                                              expiration_date=post_serialized_data.validated_data['expirationDate'],
                                              password=post_serialized_data.validated_data['password'])

        return response_service(paste_object.paste_hash, True, "Paste Added")

    def get(self, request):

        content_hash = request.query_params.get('id', None)
        password = request.query_params.get('password', None)
        user = request.user

        if content_hash:

            paste_object: Paste = Paste.objects.get(paste_hash=content_hash)

            if paste_object.visibility == Paste.VisibilityChoice.PRIVATE:
                if user and paste_object.user.id == user.id:
                    if paste_object.password and password and paste_object.password == password:
                        return response_service(paste_response(paste_object), True, "Paste Found")
                    else:
                        return response_service("password required not in query param", False, "paste is password protected")

                else:
                    return response_service("not authenticated user", False, "private paste")

            else:
                return response_service(paste_response(paste_object), True, "Paste Found")
        else:
            return response_service("INVALID_INPUT", False, "id required in query_param")


def paste_response(paste: Paste):
    return {
        "pasteHash": paste.paste_hash,
        "title": paste.title,
        "contentUrl": paste.content_url,
        "formatter": paste.formatter,
        "createdOn": paste.created_on,
        "updatedOn": paste.updated_on,
        "expirationDate": paste.expiration_date
    }


def response_service(data: object, is_success: bool, message: str) -> RestResponse:
    response_text = {
        "data": data,
        "message": message,
        "status": 200 if is_success else 400,
        "error": False if is_success else True
    }
    return RestResponse(response_text)
