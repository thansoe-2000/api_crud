from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    

    # task comment
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    # task end

    # language comment
    path('language-list/', views.languageList, name='language-list'),
    path('language-detail/<str:pk>/', views.languageDetail, name='language-detail'),
    path('language-create/', views.languageCreate, name="language-create"),
    path('language-update/<str:pk>/', views.languageUpdate, name="language-update"),
    path('language-delete/<str:pk>/', views.languageDelete, name="language-delete"),



]
