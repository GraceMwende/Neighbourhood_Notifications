from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
  neighbourhood_name = models.TextField()
  neighbourhood_location = models.TextField()
  occupants_count = models.IntegerField()
  # admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

  def __str__(self):
    return self.neighbourhood_name

  def save_neighbourhood(self):
    self.save()

  def delete_neighbourhood(self):
    self.delete()

  @classmethod
  def display_neighbourhhoods(cls):
    neighbourhoods = cls.objects.all()
    return neighbourhoods

class Users(models.Model):
  user_name = models.CharField(max_length=30)
  user_id = models.IntegerField()
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  email_address = models.EmailField()

class Business(models.Model):
  business_name = models.CharField(max_length=30)
  users = models.ForeignKey(Users, on_delete=models.CASCADE)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  business_email_address = models.EmailField()

class Profile(models.Model):
  user =  models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg',upload_to='profile_pics')

class Post(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='posts/')
  post = HTMLField()
  comments = models.TextField(max_length=500)
  pub_date = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return f'{self.user.username} Profile'

  def save_post(self):
    self.save()

  def delete_post(self):
    self.delete()

  @classmethod
  def display_posts(cls):
    posts = cls.objects.all()
    return posts