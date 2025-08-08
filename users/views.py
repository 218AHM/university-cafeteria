from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # built-in auth login url
    template_name = 'registration/signup.html'



class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'  # we'll create this
    next_page = reverse_lazy('home')            # redirect after logout