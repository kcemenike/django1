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

#### 2
Include it in the view.py file
Create a function that displays 'hello world'
`from django.http import HttpResponse`

`def myView(request):`
`    return HttpResponse(" Hello World")`

