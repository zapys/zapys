from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import CustomUser
from django.shortcuts import get_object_or_404
from .forms import SignupForm

# from django.urls import reverse_lazy
# from django.views.generic import CreateView

# class SignUpView(CreateView):
#     form_class = SignupForm
#     success_url = reverse_lazy("index")
#     template_name = "registration/signup.html"


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context=context)
