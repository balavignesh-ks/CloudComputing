from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # /movies/
    path('', views.index, name='index'),
    
    # /movies/id e.g. /movies/1
    path('<int:movie_id>/', views.show, name='show'),
    
    # /movies/add
    path('add/', views.add, name='add'),
    
    # /movies/id/edit
    path('<int:movie_id>/edit/', views.edit, name='edit'),
    
    # /movies/id/remove
    path('<int:movie_id>/remove/', views.remove, name='remove'),
]
