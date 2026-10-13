from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Attempt

def enter(request):
    error = ""

    if request.method == "POST":
        name = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = User.objects.filter(username=name).first()

        if user and not user.is_active:
            error = "Вы заблокированы. Обратитесь к администратору"
        else:
            u = authenticate(request, username=name, password=password)

            if u:
                a, _ = Attempt.objects.get_or_create(user=u)
                a.count = 0
                a.save()
                login(request, u)
                return redirect("/admin/" if u.is_staff else "/home/")

            error = "Вы ввели неверный логин или пароль. Пожалуйста проверьте ещё раз введенные данные"

            if user:
                a, _ = Attempt.objects.get_or_create(user=user)
                a.count += 1
                a.save()

                if a.count >= 3:
                    user.is_active = False
                    user.save()

    return render(request, "login.html", {"error": error})


@login_required
def home(request):
    return HttpResponse("Вы успешно авторизовались")
