from django.contrib.auth.forms import UserCreationForm, User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Profile
 
 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def user_profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'user/profile.html', {"User": User.objects.filter(id=request.user.id)})
