from django.shortcuts import render


def main(request):
    return render(request, "app_quotes/index.html", context={"title": "Homework 2.10 Django"})