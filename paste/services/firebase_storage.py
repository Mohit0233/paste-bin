import os
import uuid
# import paste.services.request_logging
from firebase_admin import credentials, initialize_app, storage


# Init firebase with your credentials

def init():
    try:

        cred = credentials.Certificate(os.getcwd() + '/paste/credentials/cred-firebase.json')
    except FileNotFoundError:
        cred = credentials.Certificate(os.getcwd() + '/../credentials/cred-firebase.json')
    initialize_app(cred, {'storageBucket': 'paste-bin-be890.appspot.com'})


def update_media_and_get_url(data, content_type):
    bucket = storage.bucket()
    blob = bucket.blob('pastes/' + uuid.uuid4().__str__() + '.txt')
    # blob.upload_from_filename(file_name)
    blob.upload_from_string(data)
    # Opt : if you want to make public access from the URL
    blob.make_public()
    print("public url generated: ", blob.public_url)

    return blob.public_url


init()
# update_media_and_get_url("Hello Firebase Storage", 'text/plain')
