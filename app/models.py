from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib import admin
# Create your models here.

    

class ChatConversation(models.Model):
    #userid = models.IntegerField(unique=True)
    session_id = models.CharField(max_length=1000)
    bot_message = models.CharField(max_length=10000,null=True)
    user_message = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically record creation time
    class meta:
        ordering = ['-timestamp','-session_id']

    def __str__(self):
        return f"{self.timestamp}" + " - " + f"{self.session_id}"


class query(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name + " - " + str(self.time)

STATUS = ((0, "Draft"),(1, "Publish"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug  = models.SlugField(max_length=200, unique=True)
    #heading = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    subheading = models.CharField(max_length=120,unique=True)
    imali = models.URLField()
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title



#booking meeting model

# booking/models.py

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title

class Seat(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Meeting: {self.meeting.title}, Seat: {self.seat_number}"

