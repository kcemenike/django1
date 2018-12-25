from django.shortcuts import render
# from django.http import HttpResponse

# =============================================================================
# Old version of todoView to show the content of todo.html template only
# def todoView(request):
#     # return HttpResponse('Hello this is a todo app')
#     return render(request, 'todo.html')
# =============================================================================


from .models import todoItem
from django.http import HttpResponseRedirect

def todoView(request):
    # This function shows not just the html template, but also interacts with the sqlite DB
    return render(request, 'todo.html', {'all_items': todoItem.objects.all()})
    # the {'all items':todoItems.objects.all()} is a list of all items that we will loop through in the todo.html

# function to add item to todo
def todoAdd(request):
    # create a new todo item
    new_item = todoItem(content = request.POST['content'])
    # save
    new_item.save()
    # redirect the browser to /todo/
    return HttpResponseRedirect('/todo/')

def todoDel(request, todo_id):
    # get todo Item
    item_to_del = todoItem.objects.get(id=todo_id)
    # delete
    item_to_del.delete()
    # save
    return HttpResponseRedirect('/todo/')
    

# Create your views here.
