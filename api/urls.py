from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', TaskCreateAPIview.as_view()),
    path("admin/<int:pk>/delete/", TaskDeleteAPIview.as_view()),
    path("admin/<int:pk>/", TaskDetailAPIview.as_view()),
    path("admin/<int:pk>/update/", TaskUpdateAPIview.as_view()),
    
    path('', TaskUserCreateAPIview.as_view()),
    path("<int:pk>/delete/", TaskUserDeleteAPIview.as_view()),
    path("<int:pk>/", TaskUserDetailAPIview.as_view()),
    path("<int:pk>/update/", TaskUserUpdateAPIview.as_view())
    
    
]
