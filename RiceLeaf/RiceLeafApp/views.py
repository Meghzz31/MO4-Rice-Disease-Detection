from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.db import transaction


from .models import *
from .forms import *
from .predict import process
from .utils import chat_with_rasa
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.db.models import F, Value, IntegerField, Sum,Q,Max
from django.db.models.functions import Cast

from django.conf import settings
import os

# Create your views here.
def index(request):
    return render(request,'index.html')

def logout(request):
    request.session.clear()
    return redirect('index')

def login_view(request,user_type):
    return render(request,'auth/login.html',{'user_type':user_type})

def register_view(request,user_type):
    return render(request,'auth/register.html',{'user_type':user_type})

def createAccount(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            response = {
                'status': True,
                'message': 'User Created Successfully'
            }
            return JsonResponse(response)
        else:
            # Form is not valid, extract error messages
            errors = form.errors
            print(errors)
            error_message = str(errors['contact'][0]) if 'contact' in errors else str(errors['email'][0]) if 'email' in errors  else 'Invalid form data'

            response = {
                'status': False,
                'message': error_message
            }
            return JsonResponse(response)
        
    return JsonResponse({ 'status':False, 'message':'Invalid Request Method!' })

def loginAccount(request):
    if request.method=='POST':
        response={
            'status':False,
            'message':'Invalid Request Method!'
        }
           
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']
        
        user = User.objects.filter(email=email, password=password,is_active=1,user_type=user_type).first()

        if user is None:
            response={
                'status':False,
                'message':'Invalid User'
            }
        else:
            request.session['userId']=user.id
            request.session['user_type']=user.user_type
            
            response={
                'status':True,
                'message':'Successfully logged in'
            }
           
    return JsonResponse(response)


def home_view(request):
    return render(request,'home/home.html')

def gallery_view(request):
    data = [
        {
           # 'title': 'Basmati Rice',
            'place': 'Konaje, Mangalore',
            'image': '/media/gallery/image1.jpg'
        },
        {
           # 'title': 'Jasmine Rice',
            'place': 'Talapady, Mangalore',
            'image': '/media/gallery/image2.jpg'
        },
        {
           # 'title': 'Arborio Rice',
            'place': 'Ullal, Mangalore',
            'image': '/media/gallery/image3.jpg'
        },
        {
           # 'title': 'Sushi Rice',
            'place': 'Boliyar, Mangalore',
            'image': '/media/gallery/image5.jpg'
        },
        {
           # 'title': 'Brown Rice',
            'place': 'Harekala, Mangalore',
            'image': '/media/gallery/image6.jpg'
        },
        {
           # 'title': 'Wild Rice',
            'place': 'Kenjar, Mangalore',
            'image': '/media/gallery/image7.jpg'
        },
        {
           # 'title': 'Glutinous Rice (Sticky Rice)',
            'place': 'Thumbe, Mangalore',
            'image': '/media/gallery/image8.jpg'
        },
        {
           # 'title': 'Wild Rice',
            'place': 'Alepady, Mangalore',
            'image': '/media/gallery/image9.jpg'
        },
        {
           # 'title': 'Glutinous Rice (Sticky Rice)',
            'place': 'Thokottu, Mangalore',
            'image': '/media/gallery/image10.jpg'
        },
        {
           # 'title': 'Glutinous Rice (Sticky Rice)',
            'place': 'Bolar, Mangalore',
            'image': '/media/gallery/image11.jpg'
        },
        {
           # 'title': 'Glutinous Rice (Sticky Rice)',
            'place': 'Konekal, Mangalore',
            'image': '/media/gallery/image12.jpg'
        },
        {
           # 'title': 'Glutinous Rice (Sticky Rice)',
            'place': 'Harekala, Mangalore',
            'image': '/media/gallery/image13.jpg'
        }
    ]

    return render(request,'home/gallery.html',{'data':data})

def upload(request):
    return render(request,'home/upload.html')

def detect_disease(request):
    if request.method == 'POST':

        image = request.FILES['image']

        image_name = 'input.png'
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)

        with open(image_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        
        result = process(image_path)

        print(result)
    
        return JsonResponse({ 'status':True, 'message':"Success",'data':result })
    else:
        return JsonResponse({ 'status':False, 'message':'Invalid Request Method!' })

def chatbot(request):
    if request.method =='POST':
        user_input = request.POST['chat_input']
        response = chat_with_rasa(request,user_input)
        print(response)
        return JsonResponse(response,safe=False)
    return render(request,'home/chatbot.html')