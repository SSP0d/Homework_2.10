from django.shortcuts import render


def main(request):
    return render(request, "app_users/login.html", context={"title": "Login page"})