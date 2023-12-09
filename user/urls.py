from django.urls import path
from .views import register_user,CustomUSerToken,LoginView


urlpatterns = [
    path('register/', register_user, name='register'),
    path('token/', CustomUSerToken.as_view(), name='token'),
    path('login/', LoginView.as_view(), name='login'),
]
