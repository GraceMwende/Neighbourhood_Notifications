from django.urls import path,re_path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('',views.home,name='home'),
  path('tinymce/',include('tinymce.urls')),
  path('new/post/',views.new_post,name='new-post'),
  re_path('post/(\d+)',views.posts, name='posts'),
  path('addcomment/<int:id>/',views.add_comment,name='add_comment'),
  path('new/business',views.new_business, name='new-business'),
  path('business/',views.business,name='business')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)