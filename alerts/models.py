from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
  neighbourhood_name = models.TextField()
  neighbourhood_location = models.TextField()
  occupants_count = models.IntegerField()
  health = models.CharField(max_length = 100, default='health@gmail.com')
  police = models.CharField(max_length = 100, default='police@gmail.com')

  # admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

  def __str__(self):
    return self.neighbourhood_name

  def create_neighbourhood(self):
    self.save()

  

  @classmethod
  def display_neighbourhhoods(cls):
    neighbourhoods = cls.objects.all()
    return neighbourhoods

  @classmethod
  def delete_neighbourhood(cls,id):
    self.objects.filter(id=id).delete()

  @classmethod
  def find_neigborhood(cls,neigborhood_id):
    neighbour = cls.objects.filter(id= neigborhood_id)
    return neighbour

class Users(models.Model):
  user_name = models.CharField(max_length=30)
  user_id = models.IntegerField()
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  email_address = models.EmailField()

class Business(models.Model):
  business_name = models.CharField(max_length=30)
  users = models.ForeignKey(User, on_delete=models.CASCADE)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  business_email_address = models.EmailField()

  def __str__(self):
    return f'{self. business_name} '

  def save_business(self):
    self.save()

  @classmethod
  def delete_business(cls,id):
    self.objects.filter(id=id).delete()

  @classmethod
  def find_business(cls,id):
    neighbour = cls.objects.filter(id= id)
    return neighbour

  @classmethod
  def display_business(cls):
    posts = cls.objects.all()
    return posts

class Profile(models.Model):
  user =  models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg',upload_to='profile_pics')

class Post(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='posts/')
  post = HTMLField()
  pub_date = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return f'{self.user.username}'

  def save_post(self):
    self.save()

  def delete_post(self):
    self.delete()

  @classmethod
  def display_posts(cls):
    posts = cls.objects.all()
    return posts

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.TextField(max_length=1000)

  def __str__(self):
    return self.user.username