from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import Signupform
from .models import CustomUser
from django.shortcuts import get_object_or_404


def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = Signupform()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context=context)