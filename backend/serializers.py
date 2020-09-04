from rest_framework import serializers
from backend.models import *
from rest_framework import status

class Contactusserializer (serializers.Serializer):
     class Meta:
         modal=Contactus
         fields = '__all__'


# class PostCommentSerializer(serializers.ModelSerializer):
      
#     profilephoto=serializers.SerializerMethodField()
    
   
  
#     class Meta:
#         model = PostComment
#         fields = ['id','commented_by','content','date','profilephoto','replypostcomment']

#     def get_commented_by(self, obj):
#         return obj.commented_by

#     def get_post(self, obj):
#         return obj.post.title

#     def get_profilephoto(self,obj):
#         if profileDB.objects.all().filter(user=obj.commented_by).count()>0:
#             profile=profileDB.objects.all().filter(user=obj.commented_by)
#             print(profile)
#             return profile[0].profilephoto.url
#         else:
#             print("---------------------->")



# class PostSerializer(serializers.ModelSerializer):
    
    
    
#     likes = serializers.SerializerMethodField()
#     likes_count = serializers.SerializerMethodField()
#     postcomment = PostCommentSerializer(many=True)
#     posted_on = serializers.DateTimeField(source='FORMAT')
#     profilephoto=serializers.SerializerMethodField()
    
#     class Meta:
#         model = Post
#         fields = ['id', 'isPosted', 'posted_by', 'posted_on', 'title', 'cover','file', 'content', 'language', 'category',
#                   'tagpost', 'playlist','type','likes','likes_count', 'postcomment','profilephoto']


#     def get_posted_by(self, obj):
#         return obj.posted_by

#     def get_profilephoto(self,obj):
#         if profileDB.objects.all().filter(user=obj.posted_by).count()>0:
#             user=profileDB.objects.all().filter(user=obj.posted_by)
#             print(user[0].first_name)
#             return user[0].profilephoto.url
#         else:
#             print("---------------------->")

#     def get_likes(self, obj):
#         p =obj.likes.all()
#         lst = []
#         for i in range(len(p)):
#             lst.append({"id": p[i].id, "username": p[i].username})
#         return lst

#     def get_tagpost(self, obj):
#         p =obj.tagpost.all()
#         lst = []
#         for i in range(len(p)):
#             lst.append({"id": p[i].id, "created_by": p[i].created_by,"tag": p[i].tag ,\
#                  "type":p[i].tag_type,\
#                 "created_at":p[i].created_at})
#         return lst
    
#     def get_likes_count(self, obj):
#         return obj.likes.count()