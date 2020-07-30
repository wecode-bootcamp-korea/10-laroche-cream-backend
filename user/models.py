from django.db import models
from product.models import *

class User(models.Model):
    name            = models.CharField(max_length = 50, default = "")
    account         = models.CharField(max_length = 100, default = "")
    password        = models.CharField(max_length = 100, default = "")
    birthday        = models.CharField(max_length = 100, null = True)
    gender_type     = models.ForeignKey('Gender', on_delete = models.CASCADE, null = True)
    email           = models.CharField(max_length = 200, default = "")
    phoneNumber     = models.CharField(max_length = 100, default = "")
    skinType        = models.ForeignKey('SkinType', on_delete = models.CASCADE, null = True)
    skinTrouble     = models.ManyToManyField('SkinTrouble', through = 'UserSkinTrouble')
    likeProduct     = models.ManyToManyField(Product, through = 'LikeProduct', related_name = 'like_product')
    skinSensitivity = models.IntegerField(default = 0)
    created_at      = models.DateTimeField(auto_now_add = True, null = True)
    updated_at      = models.DateTimeField(auto_now = True, null = True)
    
    class Meta:
        db_table = "users"

class Gender(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "genders"

class SkinType(models.Model):
    name = models.CharField(max_length = 50, null=True)

    class Meta:
        db_table = "skin_types"

class UserSkinTrouble(models.Model):
    user        = models.ForeignKey('User', on_delete = models.CASCADE)
    skinTrouble = models.ForeignKey('SkinTrouble', on_delete = models.CASCADE)
    
    class Meta:
        db_table = "user_skin_troubles"

class SkinTrouble(models.Model):
    name = models.CharField(max_length = 50, default = " ")

    class Meta:
        db_table = "skin_troubles"

class LikeProduct(models.Model):
    user    = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        db_table = "likeproducts"

class CartProduct(models.Model):
    user    = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        db_table = "cartproducts"


