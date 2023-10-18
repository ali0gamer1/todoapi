from django.urls import path
from .views import *
urlpatterns = [
    path('', TaskCreateAPIview.as_view()),
    path("<int:pk>/delete/", TaskDeleteAPIview.as_view()),
    path("<int:pk>/", TaskDetailAPIview.as_view()),
    path("<int:pk>/update/", TaskUpdateAPIview.as_view())
    
    
]
