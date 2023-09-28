from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
     api_urls = {

          # Task comments
          'Task List':'/task-list/',
          'Task Detail':'/task-detail/<str:pk>/',
          'Task Create':'/task-create/',
          'Task Update':'/task-update/<str:pk>/',
          'Task Delete':'/task-delete/<str:pk>/',

          # language comments
          'Language List':'/language-list/',
          'Language Detail':'/language-detail/<str:pk>/',
          'Language Create':'/language-create/',
          'Language Update':'/language-update/<str:pk>/',
          'Language Delete':'/language-delete/<str:pk>/',


     }
     return Response(api_urls)

@api_view(['GET'])
def taskList(request):
     tasks = Task.objects.all()
     serializer = TaskSerializer(tasks, many=True)
     return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
     task = Task.objects.get(id=pk)
     serializer = TaskSerializer(task, many=False)
     return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
     serializer = TaskSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
     task = Task.objects.get(id=pk)
     serializer = TaskSerializer(instance=task, data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
     task = Task.objects.get(id=pk)
     task.delete()
     return Response("Item successfully delete!")


@api_view(['GET'])
def languageList(request):
     languages = Language.objects.all()
     serializer = LanguageSerializer(languages, many=True)
     return Response(serializer.data)

@api_view(['GET'])
def languageDetail(request, pk):
     language = Language.objects.get(id=pk)
     serializer = LanguageSerializer(language, many=False)
     return Response(serializer.data)


@api_view(['POST'])
def languageCreate(request):
     serializer = LanguageSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)

@api_view(['POST'])
def languageUpdate(request, pk):
     language = Language.objects.get(id=pk)
     serializer = LanguageSerializer(instance=language, data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)

@api_view(['DELETE'])
def languageDelete(request, pk):
     language = Language.objects.get(id=pk)
     language.delete()
     return Response("Language successfully delete!")
