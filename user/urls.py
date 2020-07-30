from django.urls import path
from .views import SignUpView, SignInView, LikeProductView, CartProductView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/likeproduct', LikeProductView.as_view()),
    path('/cartproduct', CartProductView.as_view())
]
