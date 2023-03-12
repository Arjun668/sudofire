from django.urls import path, include
from authentication.social_views import GoogleLogin

urlpatterns = [
    path('google-login/', GoogleLogin.as_view(), name="google-login"),
]