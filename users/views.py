from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from users.models import User
from users.serializers import UserSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    return HttpResponse("<h1>Home<h1>")

def user_list(request):
    # GET list of users:
    if request.method == 'GET':
        users = User.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            users = users.filter(name__icontains=name)
        
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
   # find tutorial by pk (id)
    try: 
        user = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        users_serializer = UserSerializer(user) 
        return JsonResponse(users_serializer.data) 

    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        users_serializer = UserSerializer(user, data=user_data) 
        if users_serializer.is_valid(): 
            users_serializer.save() 
            return JsonResponse(users_serializer.data) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE': 
        user.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)