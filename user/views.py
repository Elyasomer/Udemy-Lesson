from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    return render(request, "login_page.html", context)
