from django.shortcuts import render

def file_list_view(request, *args, **kwargs):
    return render(request, "base/base.html", {})