from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def home(request):
    return HttpResponse("hello, wolrd! hollodjango")


def api(request):
    data = {
        "1": {
            "title": "مقاله اول",
            "id": "20",
            "slug": "first-article"
        },
        "2": {
            "title": "مقاله دوم",
            "id": "21",
            "slug": "second-article"
        },
        "3": {
            "title": "مقاله سوم",
            "id": "22",
            "slug": "third-article"
        }

    }
    return JsonResponse(data)
