import base64
from django.conf import settings

def get_reed_auth_header():
    api_key = settings.REED_API_KEY
    token = f"{api_key}:".encode("utf-8")
    encoded = base64.b64encode(token).decode("utf-8")
    return {
        "Authorization": f"Basic {encoded}"
    }  


