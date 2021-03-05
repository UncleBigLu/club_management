from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .templates.register.form import MyCreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    form = MyCreateUserForm()

    # Register the user
    if request.method == 'POST':
        form = MyCreateUserForm(request.POST)
        if form.is_valid():
            # Register success
            form.save()

            # Get the user name
            uname = form.cleaned_data.get('username')
            # Add a flash message
            messages.success(request, uname + ' register success!')
            # Display the message

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a user
            # hit the Back button.
            return HttpResponseRedirect('login')

    context = {'form': form}
    return render(request, 'register/register.html', context)


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passwd = request.POST.get('password')

        user = authenticate(request, username=uname, password=passwd)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('login')

    context = {}
    return render(request, 'register/login.html', context)
