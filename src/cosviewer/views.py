from django.shortcuts import render

def file_list_view(request, *args, **kwargs):
    return render(request, "views/login.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "views/login.html", {})