from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'), (1, 'Publish'))

# Create your models here.

# the below class will create a 'Post' table which we can view in our db.sqlite3 database

class Post(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True) #when a blog post is created, current date and time will be injected into this 'date_created' field of the table
    slug = models.SlugField(max_length=200, unique =True) # this is the extension to the url where this table will be used 
    author = models.ForeignKey(to = User, on_delete= models.CASCADE) # This means if a user is deleted from the database, the users posts will also be deleted
    status = models.IntegerField(choices=STATUS, default= 0) 