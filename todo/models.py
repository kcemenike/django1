from django.db import models
# Create your models here.

# This class represents each todo object when instantiated
class todoItem(models.Model):
    content = models.TextField() # This is an attribute of the todoItem that represents the content of the object
    