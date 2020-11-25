from django.urls import path     
from . import views
urlpatterns = [
     path('firstpath/', views.index),
    # path('secondpath/<int:id>', views.index2),
    path('', views.root_method),

    path('blogs/', views.index ),
     path('blogs/new', views.new ),
     path('blogs/create', views.create ),
     path('blogs/<int:num>', views.show ),
     path('blogs/<int:num>/edit', views.edit ),
     path('blogs/<int:num>/delete', views.destroy ),
    #  path('blogs/json', views.jsonreturn ),
 
]