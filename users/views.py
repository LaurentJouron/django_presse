from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from .forms import UserCreationForm


def signup(request):
    if request.method != "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect("home:home")
        else:
            form = UserCreationForm()
            context = {"form": form}
        return render(request, "users/signup.html", context=context)
