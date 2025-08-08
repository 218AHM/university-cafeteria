"""
URL configuration for uni_cafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from cafeteria.views import menu, home, order, order_success
from uni_cafe import settings
from django.contrib.auth import views as auth_views
from users.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home", home, name="home"),
    path("", auth_views.LoginView.as_view(template_name="registration/login.html"), name="main"),
    path("menu/", menu, name="menu"),
    path("order/", order, name="order"),
    path("order/success", order_success, name="order_success"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include('users.urls')),
    path("signup/", SignUpView.as_view(), name="signup")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
