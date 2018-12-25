from django.shortcuts import render
from django.http import HttpResponse

def todoView(request):
    # return HttpResponse('Hello this is a todo app')
    return render(request, 'todo.html')

# Create your views here.
