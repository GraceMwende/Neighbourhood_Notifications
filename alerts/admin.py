from django.contrib import admin
from .models import Profile,Users,Neighbourhood,Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(Users)
admin.site.register(Neighbourhood)
admin.site.register(Business)