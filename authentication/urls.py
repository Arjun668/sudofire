from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication.views import LoginApiViewset,RegisterViewset

app_name = "account"
trailing_slash = False

urlpatterns = [
    # path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', LoginApiViewset.as_view(), name='login'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
       
    path('register/', RegisterViewset.as_view({'post': 'create'}), name='register'),
    path('user-lists/', RegisterViewset.as_view({'get': 'list'}), name='user-list'),
]