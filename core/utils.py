import jwt
import json
import requests

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import SECRET_KEY
from user.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
            user = User.objects.get(account=payload['account'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper
