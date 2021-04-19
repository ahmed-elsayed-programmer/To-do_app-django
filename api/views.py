from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list',
        'Delet': '/task-delete',
        'update': '/task-update',
        'create': '/task-create',
    }

    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    seializer = TaskSerializers(tasks , many=True )
    return Response(seializer.data)

@api_view(['GET'])
def taskdetale(request , pk):
    tasks = Task.objects.get(id =pk)
    seializer = TaskSerializers(tasks , many=False )
    return Response(seializer.data)

@api_view(['POST'])
def taskcreat(request):
    serializer = TaskSerializers(data = request.data)

    if serializer.is_valid() :
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request ,pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializers(instance=task ,data = request.data)

    if serializer.is_valid() :
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE'])
def taskdelete(request ,pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response('Item succesfuly delted')