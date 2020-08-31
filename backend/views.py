from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from backend.models import *
from django.core.mail import send_mail

@api_view(['POST'])
def contact_create(request):
    serializer = Contactusserializer(data=request.data)
    q=Contactus.objects.create(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email'],
        text=request.data['text']
    )
    print(request.data)
    if serializer.is_valid():
        q.save()
    return Response(request.data,status=status.HTTP_201_CREATED)


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