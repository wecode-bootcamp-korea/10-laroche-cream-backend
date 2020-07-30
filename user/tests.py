import json
import bcrypt
import datetime

from django.test import TestCase, Client
from .models import User, Gender, SkinType, SkinTrouble, UserSkinTrouble

class SignUpTest(TestCase):

    def setUp(self):
        Gender.objects.create(
            name='남자'
        )

        Gender.objects.create(
            name='여자'
        )

        SkinType.objects.create(
            name='건성'
        )
        
        SkinType.objects.create(
            name='복합성'
        )

        SkinType.objects.create(
            name='중성'
        )

        SkinType.objects.create(
            name='지성'
        )

#        SkinTrouble.objects.create(
#            name='민감성 피부'
#        )

#        SkinTrouble.objects.create(
#            name='손상 피부'
#        )

        User.objects.create(name='솔안', 
                            account='solahn',
                            password='sol1414',
                            birthday='20000101',
                            email='sol@gmail.com',
                            phoneNumber='01000001111',
                            gender_type=Gender.objects.get(id=1),
                            skinType=SkinType.objects.get(id=3),
                           )

    def tearDown(self):
        User.objects.all().delete()

    def test_signupview_post_success(self):
        client = Client()
        user = {
            'name' : '안솔솔',
            'account' : 'as',
            'password' : 'as1234',
            'birthday' : '19991231',
            'email' : 'as@naver.com',
            'phoneNumber' : '01012344321',
            'gender_type' : '남자',
            'skinType' : '건성',
             }


        response = client.post('/user/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message':'SIGNUP SUCCESS'})

class SignInTest(TestCase):

    def setUp(self):
        client = Client()
        User.objects.create(
            account = 'sol',
            password = 'sol1234'
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_signin_post_success(self):
        client = Client()
        user = {
            'account' : 'sol',
            'password' : 'sol1234'
        }

        response = client.post('user/signin', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'access_token':token)

