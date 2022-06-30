from django.shortcuts import render

def board(request):
    return render(request, 'board.html')

def boardfirst(request):
    return render(request, 'boardfirst.html')
# Create your views here.
