from rest_framework import serializers
from .models import Users, Posts, Likes
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('user_id','name','email','password')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields=('post_id','title','description','content','creation_date','owner','access')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields=('like_id','user_id','post_id')