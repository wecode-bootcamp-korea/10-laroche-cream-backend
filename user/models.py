from django.db import models

class User(models.Model):
    user_name = models.IntegerField(default=0)
    user_id = models.CharField(max_length=50)
    user_pw = models.CharField(max_length=50)

class User_info(models.Model):
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)

class     

