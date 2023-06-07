from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Users, Posts, Likes
from .serializer import UserSerializer, PostSerializer, LikeSerializer
from rest_framework import status
from django.db.models import Count

# Create your views here.
@api_view(['GET'])
def index(request):
    user = Users.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAll(request):
	post = Posts.objects.all()
	count = Likes.objects.all().values("post_id").annotate(total=Count("post_id"))
	serializer = PostSerializer(post, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def getLikes(request):
	count = Likes.objects.all().values("post_id").annotate(total=Count("post_id"))
	print(count)
	return Response(count)


@api_view(['POST'])
def addUser(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
    return Response(user.data)

@api_view(['POST'])
def addPost(request):
    post = PostSerializer(data=request.data)
    if post.is_valid():
        post.save()
    return Response(post.data)

@api_view(['POST'])
def addLike(request):
    like = LikeSerializer(data=request.data)
    if like.is_valid():
        like.save()
    return Response(like.data)


#retrieval

@api_view(['GET'])
def getUser(request, id):
    user = Users.objects.get(user_id=id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPost(request, id):
	post = Posts.objects.get(post_id=id)
	if(post.access=='1'):
		post = Posts.objects.get(post_id=id)
		serializer = PostSerializer(post, many=False)
		return Response(serializer.data)
	if(post.owner==request.user):
		post = Posts.objects.get(post_id=id)
		serializer = PostSerializer(post, many=False)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getLike(request, id):
    like = Likes.objects.get(like_id=id)
    serializer = LikeSerializer(like, many=False)
    return Response(serializer.data)

#update api

@api_view(['POST'])
def updateUser(request, id):
	item = Users.objects.get(user_id=id)
	data = UserSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def updatePost(request, id):
	item = Posts.objects.get(post_id=id)
	data = PostSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def updateLike(request, id):
	item = Likes.objects.get(like_id=id)
	data = LikeSerializer(instance=item, data=request.data)
	print(data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

#delete apis

@api_view(['DELETE'])
def deleteUser(request, id):
	item = Users.objects.get(user_id=id)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def deletePost(request, id):
	item = Posts.objects.get(post_id=id)
	if(item.owner==request.user):
		item.delete()
		return Response(status=status.HTTP_202_ACCEPTED)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteLike(request, id):
	item = Likes.objects.get(like_id=id)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
