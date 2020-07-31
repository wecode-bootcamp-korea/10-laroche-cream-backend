import datetime
import json
import bcrypt
import jwt

from django.views     import View  
from django.http      import (
    HttpResponse, 
    JsonResponse
)    

from my_settings      import SECRET_KEY
from user.models      import (
    User, 
    Gender, 
    SkinType,
    UserSkinTrouble,
    SkinTrouble
)
from core.utils import login_decorator

class SignUpView(View):
    def post(self, request):
        user_data = json.loads(request.body)
        try:
            if User.objects.filter(account = user_data['account']).exists():
                return JsonResponse({'message':'DUPLICATED ID'}, status=400)


            User(
                name        = user_data['name'],
                account     = user_data['account'],
                password    = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt()).decode(),
                email       = user_data['email'],
                birthday    = user_data['birthday'],
                gender_type = Gender.objects.get(name = user_data['gender_type']),
                phoneNumber = user_data['phoneNumber'],
                skinType = SkinType.objects.get(name = user_data['skinType']),
                skinSensitivity = user_data['skinSensitivity']
            ).save()

            UserSkinTrouble(
                user = User.objects.get(account = user_data['account']),
                skinTrouble = SkinTrouble.objects.get(name = user_data['skinTrouble'])

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
                    token = jwt.encode({'user_id':user.id}, 'secret', algorithm='HS256').decode('utf-8')
                    return JsonResponse({'access_token':access_token}, status=200)
                
                return JsonResponse({'message':'UNAUTHORIZED'}, status=401)

            return JsonResponse({'message':'INVALID_USER'}, status=400)

        except KeyError:
            return JsonResponse({'message':'KEYERROR'}, status=400)
                