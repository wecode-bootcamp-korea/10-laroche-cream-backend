from django.urls import path
from .views import SignUpView, AccountCheckView, SignInView, UserInfoView, LikeProductView, CartProductView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/accountcheck', AccountCheckView.as_view()),
    path('/userinfo', UserInfoView.as_view()),
    path('/likeproduct', LikeProductView.as_view()),
    path('/cartproduct', CartProductView.as_view())

