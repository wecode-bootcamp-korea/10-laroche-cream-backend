import jwt
import json
import requests

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import SECRET_KEY
from user.models import User

class Login_required:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, request, *args, **kwargs):
        access_token = request.headers.get("Authorization", None)
        try:
            if access_token:
                payload = jwt.decode(access_token, "secret", algorithms="HS256")
                user = User.objects.get(account=payload['account'])
                request.user = user
                return self.original_function(self, request, *args, **kwargs)

        
            return JsonResponse({'message': 'LOGIN_PLEASE'}, status=401)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'EXPIRED_TOKEN'}, status=401)

        except jwt.DecodeError:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

