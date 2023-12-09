from django.urls import path
from .views import register_user,CustomUSerToken


urlpatterns = [
    path('register/', register_user, name='register'),
    path('token/', CustomUSerToken.as_view(), name='token'),
]
