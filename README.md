# django1
let's see what Django can do...

### Step 1:
#### Using Anaconda
- Create environment, either using Anaconda > Environment > Create, then install django in the virtual environment created
- Right click on the environment created, then click run terminal and create a folder of your choice to host the project files
- navigate to the folder, and run `django-admin startproject projectname .`
OR 
#### Using pipenv
Installing pipenv (pip3 install pipenv) and running pipenv install django=versionnumber
Create a folder of your choice to host the project, then run pipenv shell inside the project
Run `django-admin startproject projectname .` inside the project folder

### Step 2
Startup django server by running
<br>`python manage.py runserver`

## Create an app
To create an app, use startapp. That is:
<br>`python manage.py startapp hello`
creates an app with the name hello
This creates a subfolder in the project folder with a couple of items you can edit

To connect the main project with this newly created app, you need to :
#### 1
include the INSTALLED_APPS section of the settings.py file
```
INSTALLED_APPS = [`
    .`
    .`
    .`    
    'django.contrib.staticfiles',`
    'hello', # recall that this is the app name, not the page name`
]
```

#### 2
Include it in the view.py file
Create a function that displays 'hello world'
```
from django.http import HttpResponse`

def myView(request):
    return HttpResponse(" Hello World")
```
***
# Let's create a ToDo app
As usual, run `python manage.py startapp todo` to create the app
A todo folder is created
Add 'todo' to the INSTALLED_APPS section of settings.py of the project folder
Add the todoView function to views.py in the app folder (remember to import HttpResponse from django.http)
Then run `python manage.py runserver`
This should show just text. But we need to show more than just that
Here we need to create a template
Create a templates folder and add the todo.htmlfile to it

In the views.py, instead of having the HttpResponse('hello world') as the return statement of the text
Use `render(request, 'todo.html')` instead

To make django point to templates directory for templates, add the path to the TEMPLATES section
<br>`'DIRS': [os.path.join(BASE_DIR, 'templates')],`

### Database connect
Next step, we need to represent each todo item as an object in the database
We should use OOP to create each object in Python, and this is handled by the models.py file

Navigate to models.py and add:
```
class todoItem(models.Model):
    content = models.TextField()
```

Next, make migrations from the model to the project by running from the command line:
<br>`python manage.py makemigrations`
This creates a 0001_initial.py file that manages the migrations for the model connection to the database
To initiate the connection, run
<br>`python manage.py migrate`

### Add items to database manually
Next, let us start with manually adding items to the database (recall it is the default sqlite FB)
To connect to the python shell, run:
<br>`python manage.py shell`
This should change the terminal to a Python (or iPython terminal)
Let's add 3 items. Enter:
```
from todo.models import todoItem # This imports the todoItem function from the models.py
a = todoItem(content='permanent todo Item A') # This adds a todoItem called a
b = todoItem(content='permanent todo Item B')
c = todoItem(content='permanent todo Item C')
a.save() # This saves the todo Item a
b.save()
c.save()
```

To show the first todo Item, just run
<br>`todoItem.objects.all()[0].content`

To show all items, run
<br>
```
from i in todoItem.objects.all():
   print(i.content)
```
You can also use the get method to get the content of any item from its index
<br>`todoItem.objects.get(id=1).content`

### Display database items in browser
To show these objects in the browser (i.e. connect the database items in the view.py):
```
from .models import todoItem

def todoView(request):
    # This function shows not just the html template, but also interacts with the sqlite DB
    return render(request, 'todo.html', {'all_items': todoItem.objects.all()})
```
And in the todo.html, change the list item to the below
```
<ul>
    {% for item in all_items %}
        <li>{{item.content}}</li>
    {% endfor %}
</ul>
```

### To add items from the browser
Next, we add form block to the todo.html to add an item to the list in
```
<!- Let's add a form item-->
<form action="/addTodo/" method="post">{% csrf_token %}
    <input type="text" name="content"/>
    <input type="submit" value="Add"/>
</form>
```
Then the database action is defined in the views.py file as a todoAdd function:
```
def todoAdd(request):
    # create a new todo item
    new_item = todoItem(content = request.POST['content'])
    # save
    new_item.save()
    # redirect the browser to /todo/
    return HttpResponseRedirect('/todo/')
```

And we add the /addTodo/ path to connect to the todoAdd function in the urls.py
```
path('addTodo/', todoAdd),
```
Remember to add the function corresponding to the addTodo (i.e. todoAdd) as an import in the urls.py, i.e.
```
from todo.views import todoView, todoAdd
```


### Deleting items
To delete an item, it will be helpful to add a delete button to each item in the list
Let's change the display objects block to
```
<ul>
    {% for item in all_items %}
        <li>{{item.content}}</li>
        <form action="deltodo/{{item.id}}" method="POST">
            <input type="submit" value="Delete">
        </form>
    {% endfor %}
</ul>
```
or more elegantly (so that the button is right beside each list item:
```
<ul>
    {% for item in all_items %}
        <li>{{item.content}}
        <form   action="/deltodo/{{item.id}}/" 
                method="post"
                style="display: inline;">{% csrf_token %}
            <input type="submit" value="Delete">
        </form>
        </li>
    {% endfor %}
</ul>
```

Then add the action /deltodo/{{item.id}} to urls.py as:
```
path('deltodo/<int:todo_id>/', todoDel),
```
and then in the import
```
from todo.views import todoView, todoAdd, todoDel
```

Next we create the todoDel function in the views.py that carries out the action in the database
```
def todoDel(request, todo_id):
    # get todo Item
    item_to_del = todoItem.objects.get(id=todo_id)
    # delete
    item_to_del.delete()
    # save
    return HttpResponseRedirect('/todo/')
```