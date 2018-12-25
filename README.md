# django1
let's see what Django can do...

### Step 1:
#### Using Anaconda
- Create environment, either using Anaconda > Environment > Create, then install django in the virtual environment created
- Right click on the environment created, then click run terminal and create a folder of your choice to host the project files
- navigate to the folder, and run 'django-admin startproject projectname .'
OR 
#### Using pipenv
Installing pipenv (pip3 install pipenv) and running pipenv install django=versionnumber
Create a folder of your choice to host the project, then run pipenv shell inside the project
Run 'django-admin startproject projectname .' inside the project folder

### Step 2
Startup django server by running
    python manage.py runserver

## Create an app
To create an app, use startapp. That is:
`python manage.py startapp hello`
creates an app with the name hello
This creates a subfolder in the project folder with a couple of items you can edit

To connect the main project with this newly created app, you need to :
#### 1
include the INSTALLED_APPS section of the settings.py file
`INSTALLED_APPS = [`
`    .`
`    .`
`    .`    
`    'django.contrib.staticfiles',`
`    'hello', # recall that this is the app name, not the page name`
`]`

#### 2
Include it in the view.py file
Create a function that displays 'hello world'
`from django.http import HttpResponse`

`def myView(request):`
`    return HttpResponse(" Hello World")`

...
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
`'DIRS': [os.path.join(BASE_DIR, 'templates')],`
