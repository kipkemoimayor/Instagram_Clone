from django.db import models

# Create your models here.

class Profile(models.Model):
    pic=models.ImageField(upload_to='profile/',blank=True)
    bio=models.CharField(max_length=30)


    def __str__(self):
        return self.bio


class Image(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    name=models.CharField(max_length=30)
    captiom=models.CharField(max_length=30)
    profile=models.ForeignKey(Profile)
    likes=models.IntegerField()
    comments=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return selfself.name
