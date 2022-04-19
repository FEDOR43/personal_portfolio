from django.shortcuts import render

def index(request):
    return render(request, 'Это мое портфолио.')
