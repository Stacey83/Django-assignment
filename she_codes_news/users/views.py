from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic

from .forms import CustomUserCreationForm
from .models import CustomUser


# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
    