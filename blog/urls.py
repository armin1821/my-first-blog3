from django.urls import path
from . import views
from tarix import views as vw

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tarix/', vw.emrooz, name='emrooz'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]