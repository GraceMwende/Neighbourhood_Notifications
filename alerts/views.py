from django.shortcuts import render,redirect
from .models import Neighbourhood,Post
from .forms import NewPostForm

# Create your views here.
def home(request):
  neighbourhoods = Neighbourhood.display_neighbourhhoods()
  posts = Post.display_posts()
  return render(request,'home.html',{"neighbourhoods":neighbourhoods,"posts":posts})

def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewPostForm(request.POST,request.FILES)

    if form.is_valid():
      post = form.save(commit=False)
      post.user = current_user
      # post.profile = Profile.objects.filter(user = current_user).first()
      post.save()
    
    return redirect('home')

  else:
    form = NewPostForm()
  return render(request, 'new_post.html',{'form':form})