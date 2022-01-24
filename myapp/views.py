from django.shortcuts import render


def index(request):
    context = {'name': 'Abdulrahman'}
    return render(request, 'myapp/index.html', context)