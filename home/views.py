from django.shortcuts import redirect, render
from django.views.generic import View
from blog.forms import ArticleForm


class HomeView(View):
    def get(self, request):
        form = ArticleForm()
        context = {
            "form": form,
        }
        return render(request, "home/home.html", context=context)

    def post(self, request):
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home:home")
        context = {
            "form": form,
        }
        return render(request, "home/home.html", context=context)
