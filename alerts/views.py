from django.shortcuts import render,redirect
from .models import Neighbourhood,Post,Comment,Business
from .forms import NewPostForm,CommentForm,BusinessForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  neighbourhoods = Neighbourhood.display_neighbourhhoods()
  posts = Post.display_posts()
  return render(request,'home.html',{"neighbourhoods":neighbourhoods,"posts":posts})

def posts(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
        comments = Comment.objects.filter(post = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"post.html", {"post":post,"comments":comments})

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

def add_comment(request,id):
  if request.user.is_authenticated:
    post = Post.objects.get(id=id)

    if request.method == "POST":
      form = CommentForm(request.POST or None)
      if form.is_valid():
        data = form.save(commit=False)
        data.comment = request.POST['comment']
        data.user = request.user
        data.post = post
        data.save()

        return redirect("posts", post.id)

    else:
      form = CommentForm()
    return render(request, 'post.html',{'form':form})

  else:
    return redirect('/accounts/login')

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    
    if request.method == 'POST':
      form = BusinessForm(request.POST)

      if form.is_valid():
        business = form.save(commit=False)
        business.users = current_user
        # post.profile = Profile.objects.filter(user = current_user).first()
        business.save()
      
      return redirect('business')

    else:
      form = BusinessForm()
    return render(request, 'new_business.html',{'form':form})

def business(request):
    business = Business.display_business()
    return render(request,'business.html',{"business":business,})

    return redirect('business')

