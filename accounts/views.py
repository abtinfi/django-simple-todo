from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'], email=cd['email'], password=cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(
                request, 'user registered successefuly', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
