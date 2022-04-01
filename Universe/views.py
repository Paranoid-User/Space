from django.shortcuts import render


def start(request):
    return render(request, 'start.html')


def centre(request):
    return render(request, 'centre.html')


def end(request):
    return render(request, 'end.html')
