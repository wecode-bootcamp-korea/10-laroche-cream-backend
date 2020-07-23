import datetime
import json
import bcrypt
import jwt

from django.shortcuts import render
from django.views     import View  
from django.http      import HttpResponse, JsonResponse

from my_settings      import SECRET_KEY
from user.models      import User, Gender, SkinInfo


class SignUpView(View):
    def post(self, request):
        user_data = json.loads(request.body)
        try:
            if User.objects.filter(account = user_data['account']).exists():
                return JsonResponse({'message':'DUPLICATED ID'}, status=400)

            User.objects.create(
                name        = user_data['name'],
                account     = user_data['account'],
                password    = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt()).decode(),
                email       = user_data['email'],
                birthday    = datetime.datetime.strptime(user_data['birthday'], "%Y%m%d").date(),
                gender_type = Gender.objects.get(name = user_data['gender_type']),
                phoneNumber = user_data['phoneNumber'],
            ).save()


            SkinInfo(
                skinType        = user_data['skinType'],
                skinTrouble     = user_data['skinTrouble'],
                skinSensitivity = user_data['skinSensitivity']
            ).save()


            return JsonResponse({'message':'SIGNUP SUCCESS'}, status=200)
        
        except KeyError:
            return JsonResponse({'message':'KEYERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        user_data = json.loads(request.body)

        try:
            if User.objects.filter(account = user_data['account']).exists():
                user = User.objects.get(account = user_data['account'])

                if bcrypt.checkpw(user_data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'user_id':user.id}, 'secret', algorithm='HS256')
                    token = token.decode('utf-8')
                    return JsonResponse({'access_token':token}, status=200)
                else:
                    return JsonResponse({'message':'UNAUTHORIZED'}, status=401)

            return JsonResponse({'message':'INVALID USER'}, status=400)

        except KeyError:
            return JsonResponse({'message':'KeyError'}, status=400)
            





