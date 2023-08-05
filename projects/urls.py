from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects,name = "projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project/',views.CreateProject,name = 'createproject'),
    path('Updateproject/<str:pk>/',views.UpdateProject,name = 'Updateproject'),
    path('deleteproject/<str:pk>/',views.DeleteProject,name = 'deleteproject')

]