from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    pic=models.ImageField(upload_to='profile/',blank=True)
    bio=models.CharField(max_length=30)
    userId=models.IntegerField()


    def __str__(self):
        return self.bio

    class Meta:
        ordering=['pic']

class Comments(models.Model):
    comment=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Image(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    name=models.CharField(max_length=30)
    caption=models.CharField(max_length=30)
    likes=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    userId=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    images=models.ForeignKey(Comments,on_delete=models.CASCADE)

    def __str__(self):
        return selfself.name
    @classmethod
    def add(cls):
        pass

    class Meta:
        ordering=['image']
