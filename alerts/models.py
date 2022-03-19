from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
  neighbourhood_name = models.TextField()
  neighbourhood_location = models.TextField()
  occupants_count = models.IntegerField()
  # admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

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

  def __str__(self):
    return f'{self.user.username} Profile'