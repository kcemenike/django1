from django.shortcuts import render
from django.http import HttpResponse

# =============================================================================
# Old version of todoView to show the content of todo.html template only
# def todoView(request):
#     # return HttpResponse('Hello this is a todo app')
#     return render(request, 'todo.html')
# =============================================================================


from .models import todoItem

def todoView(request):
    # This function shows not just the html template, but also interacts with the sqlite DB
    return render(request, 'todo.html', {'all_items': todoItem.objects.all()})
# Create your views here.
