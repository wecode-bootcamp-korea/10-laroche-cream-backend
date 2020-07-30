import datetime
import json
import bcrypt
import jwt

from django.views     import View  
from django.http      import (
    HttpResponse, 
    JsonResponse
)    

from core.utils     import Login_required
from my_settings    import SECRET_KEY
from .models        import (
    User, 
    Gender, 
    SkinType, 
    SkinTrouble, 
    UserSkinTrouble, 
    LikeProduct, 
    CartProduct
)    
from product.models import *


class SignUpView(View):
    def post(self, request):
        user_data = json.loads(request.body)
        try:
            if User.objects.filter(account = user_data['account']).exists():
                return JsonResponse({'message':'DUPLICATED ID'}, status=400)

            User(
                name            = user_data['name'],
                account         = user_data['account'],
                password        = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt()).decode(),
                email           = user_data['email'],
                birthday        = user_data['birthday'],
                gender_type     = Gender.objects.get(name = user_data['gender_type']),
                phoneNumber     = user_data['phoneNumber'],
                skinType        = SkinType.objects.get(name = user_data['skinType']),
                skinSensitivity = user_data['skinSensitivity']
            ).save()

            UserSkinTrouble(
                user        = User.objects.get(account = user_data['account']),
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
                    access_token = jwt.encode({'account':user_data['account']}, 'secret', algorithm='HS256').decode('utf-8')
                    return JsonResponse({'access_token':access_token}, status=200)
                
                return JsonResponse({'message':'UNAUTHORIZED'}, status=401)

            return JsonResponse({'message':'INVALID_USER'}, status=400)

        except KeyError:
            return JsonResponse({'message':'KEYERROR'}, status=400)
            

class LikeProductView(View):
    @Login_required
    def post(self, request):
        user_data = json.loads(request.body)

        if not LikeProduct.objects.filter(product_id = user_data['product_id'], user_id = request.user.id).exists():
            LikeProduct.objects.create(
                user    = request.user,
                product = Product.objects.get(id = user_data['product_id'])
            ).save

            return JsonResponse({'message':'ADD LIKE_PRODUCT'}, status=200)

        else:
            delete_product = LikeProduct.objects.get(product_id = user_data['product_id'], user_id = request.user.id)
            delete_product.delete()

            return JsonResponse({'message':'DELETE LIKE_PRODUCT'}, status=200)

    @Login_required 
    def get(self, request):
        like_list    = []
        like_product = LikeProduct.objects.filter(user_id = request.user.id).prefetch_related("product")
        

        for product in like_product:
            data = {
                "id"           : product.product.id,
                "product_line" : product.product.product_line,
                "name"         : product.product.name,
                "price"        : product.product.price,
                "sale_price"   : product.product.sale_price,
                "hash_tag"     : product.product.hash_tag,
                "images"       : product.product.image_set.first().image_url,
                "sale"         : product.product.productflag_set.first().sale_flag,
                "gift"         : product.product.productflag_set.first().gift_flag
            }

            like_list.append(data)

        return JsonResponse({'like_list' : like_list})

class CartProductView(View):
    @Login_required
    def post(self, request):
        user_data = json.loads(request.body)
        try:
            if not CartProduct.objects.filter(product_id = user_data['product_id'], user_id = request.user.id).exists():
                CartProduct.objects.create(
                    user    = request.user,
                    product = Product.objects.get(id = user_data['product_id'])
                ).save

                return JsonResponse({'message':'ADD CART_PRODUCT'}, status=200) 
            else:
                return JsonResponse({'message': 'ALREADY_EXIST_PRODUCT'}, status=400)

        except KeyError:
            return JsonResponse({'message':'KEYERROR'}, status=200)

    @Login_required
    def get(self, request):
        cart_list    = []
        cart_product = CartProduct.objects.filter(user_id = request.user.id).prefetch_related("product")

        for product in cart_product:
            data = {
                "id"           : product.product.id,
                "product_line" : product.product.product_line,
                "name"         : product.product.name,
                "price"        : product.product.price,
                "sale_price"   : product.product.sale_price,
                "hash_tag"     : product.product.hash_tag,
                "images"       : product.product.image_set.first().image_url,
                "sale"         : product.product.productflag_set.first().sale_flag,
                "gift"         : product.product.productflag_set.first().gift_flag

            }

            cart_list.append(data)

        return JsonResponse({'cart_list' : cart_list})


