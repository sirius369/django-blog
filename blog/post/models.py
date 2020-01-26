from django.db import models
from django import forms
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import os
import random
import string

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(10))
    filename = "%s_%s.%s" % (instance.title, random_string, ext)
    return os.path.join('post_images/', filename)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    content = RichTextUploadingField(blank = True, null = True)
    preview = models.CharField(max_length = 1000)
    thumbnail  = models.FileField(upload_to = user_directory_path, default = "none.jpg")
    date = models.DateField(auto_now = False, auto_now_add = True)
    last_edit = models.DateField(auto_now = True, auto_now_add = False)
    number_of_likes = models.IntegerField(default = 0)
    number_of_comments = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(max_length = 1000)

    def __str__(self):
        return self.post.title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.post.title
