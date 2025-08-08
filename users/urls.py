from django.urls import path
from .views import SignUpView, CustomLogoutView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
