from django.urls import path
from .import views

urlpatterns = [
     path('login',views.login,name='login'),
     path('inf',views.information,name='information'),
     path('register',views.register,name='register'),
     path('create',views.create,name='create')

]
