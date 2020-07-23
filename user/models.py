from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "genders"

class User(models.Model):
    name = models.CharField(max_length=50, default=" ")
    account = models.CharField(max_length=100, default=" ")
    password = models.CharField(max_length=100, default=" ")
    birthday = models.DateField(default=0)
    gender_type = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=200, default=" ")
    phoneNumber = models.CharField(max_length=100, default=" ")
    skinInfo = models.ForeignKey('SkinInfo', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        db_table = "users"


class SkinInfo(models.Model):
    skinType = models.CharField(max_length=50, null=True)
    skinTrouble = models.CharField(max_length=100, null=True)
    skinSensitivity = models.IntegerField(default=0)

    class Meta:
        db_table = "skin_info"




