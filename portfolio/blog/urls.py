from django.urls import path
from . import views

urlpatterns = [
    path( '', views.blog, name='blog'),
    path('blog_single/', views.blog, name='blog_single')
]