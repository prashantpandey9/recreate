from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from backend.models import *
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def contact_create(request):
    serializer = Contactusserializer(data=request.data)
    print(request.data)
    q=Contactus.objects.create(
        first_name=request.data['user']['first_name'],
        last_name=request.data['user']['last_name'],
        email=request.data['user']['email'],
        text=request.data['user']['text']
    )
    
    if serializer.is_valid():
        q.save()
    return Response({"data":request.data,"status": status.HTTP_201_CREATED,"msg":"Thanks For Contacting us!!"})


# def send_mail(request):
#     ctx = {
#         'profile': "Ajay"
#     }
#     message = get_template('mail.html').render(ctx)
#     msg = EmailMessage(
#         'Subject',
#         message,
#         'noreply@wiseKreator.com',
#         ['prashantpandey94551@gmail.com'],
#     )
#     msg.content_subtype = "html"  # Main content is now text/html
#     msg.send()
#     print("Mail successfully sent")

#     return HttpResponse(f"Email sent to 1 members")
#     #return Http

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_post_comment(request, **kwargs):
#     post = get_object_or_404(Post, pk=kwargs.get('pk'))
#     if post.isPosted:
#         comment = PostComment.objects.create(post=post,
#                                              commented_by=request.user.username,
#                                              content=request.data['content'])
#         if post.posted_by != request.user.username:
#             notif = UserNotification.objects.create(userModel=User.objects.get(username=post.posted_by),
#                                                     notification=NotificationType.objects.create(
#                                                         message=f"{comment.commented_by} commented on your post {post.title}",
#                                                     icon="comment.png"),
#                                                     read=False)

#         serializer = PostCommentSerializer(comment, many=False)
#         return Response({'data': serializer.data, 'status': status.HTTP_201_CREATED})
#     else:
#         return Response({'status': 'post does not exist'})


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_post_likes(request, **kwargs):
#     post_liked = get_object_or_404(Post, pk=kwargs.get('pk'))
#     if post_liked.likes.filter(pk=request.user.pk).exists():
#         post_liked.likes.remove(request.user)
#         data = usernameSerializers(post_liked, many=False)
#         return Response({'status': status.HTTP_200_OK,'data':data.data})
#     else:
#         post_liked.likes.add(request.user)
#         data = usernameSerializers(post_liked, many=False)
#         if post_liked.posted_by != request.user.username:
#             notif = UserNotification.objects.create(userModel=User.objects.get(username=post_liked.posted_by),
#                                                     notification=NotificationType.objects.create(
#                                                         message=f"{request.user} liked your post {post_liked.title}",
#                                                         icon="heart.png"),
#                                                     read=False)
#         return Response({'status': status.HTTP_200_OK,'data':data.data})