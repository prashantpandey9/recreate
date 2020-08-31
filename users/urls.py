from django.urls import path, re_path
from users import views
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.AuthToken.as_view(), name='login'),
    path('tokenChange/', views.verifyChangeToken.as_view(), name='token'),
    path('logout/', views.Logout.as_view()),
]