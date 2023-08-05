from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def login_rq(request):
    if request.user.is_authenticated:
        messages.info(request, f"Vous êtes déjà connecté {request.user}")
        return HttpResponseRedirect("/stockage")
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"Vous êtes maintenant connecté en tant que {username}.")
                    return HttpResponseRedirect("/stockage")
                else:
                    messages.error(request, "Les informations sont invalides, veuillez réessayer")
                    return redirect("/")
            else:
                messages.error(request, "Les informations sont invalides, veuillez rééssayer.")
                return redirect("/")
        else:
            form = AuthenticationForm()
            return render(request, "stockage/login.html", {"form": form})


def register_rq(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            messages.error(request, [error.as_text()[1:] for error in form.errors.values()][0])
            return redirect("/register")
    else:
        form = NewUserForm()
        return render(request, "stockage/register.html", {"form": form})


def logout_rq(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/")
def add(request):
    "add"


@login_required(login_url="/")
def stockage(request):
    return render(request, "stockage/stockage.html")
