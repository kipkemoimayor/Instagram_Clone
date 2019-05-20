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

    def save_profile(self):
        self.save()

    def delete_profile(self):
        profile=Profile.objects.all().delete()
        return profile



class Image(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    name=models.CharField(max_length=30)
    caption=models.CharField(max_length=30)
    likes=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    userId=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    @classmethod
    def search_users(cls,term):
        result=cls.objects.filter(user__username__icontains=term)
        return result
    def save_image(self):
        self.save()

    def delete_image(self):
        image=Image.objects.all().delete()
        return image

    class Meta:
        ordering=['image']

class Comments(models.Model):
    comment=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    images=models.IntegerField()


    def update_comment(self):
        self.save()

class Followers(models.Model):
    user=models.CharField(max_length=30)
    insta=models.CharField(default='',max_length=30)
    user_id=models.IntegerField()


    def save_followers(self):
        self.save()
