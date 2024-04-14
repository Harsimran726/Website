from django.shortcuts import render
from . import models
from django.http import HttpResponse
from .models import Post
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
# Create your views here.

# views.py





def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login = models.login.objects.filter(username=username,password=password)
        if login:
            return render(request,'index.html')
        else:
            return render(request,'login.html',{'error':'Invalid username or password'})
    else:
        return render(request,'login.html')

#def register(request):
    

def your_view(request):
    client_ip = get_client_ip(request)
    print("IP address of the user machine",client_ip)

def home(request):
    return render(request,'index.html')

def product(request):
    
    return render(request,'product.html')

def services(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login = models.login.objects.filter(username=username,password=password)
        if login:
            return render(request,'index.html')
        else:
            return render(request,'login.html',{'error':'Invalid username or password'})
    else:
        return render(request,'login.html')


def user_detail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject= request.POST['subject']
        message = request.POST['message']
        query = models.query(name=name,email=email,subject=subject,message=message)
        query.save()
       
        subject = 'Thank you for filling out the form'
        message = 'We appreciate your submission.' + name + 'We will get back to you soon.'
        from_email = 'contact@bytebrainsai.online'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    # Redirect the user to a thank-you page or any desired location
        #return HttpResponseRedirect(reverse('thank_you_page'))
        return render(request,'contact.html',{'query':'Thanks for contacting us, We will get back to you soon.'})
    



def blog(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request,'blog.html',context)
    #return render(request,'blog.html')

def chatbot(request):
    Productai = models.Productai.objects.all()
    context = {'Productai': Productai}
    return render(request,'Ai chatbo.html',context)




def post(request,slug):
    postonly = Post.objects.filter(slug=slug).first()
    context = {'postonly': postonly}
    postli = []
    postli.append(postonly)
    
    return render(request,'blogbase.html',context)

#class PostList(generic.ListView):
#    queryset = models.Post.objects.filter(status=1).order_by('-created_on')
#    template_name = 'blog.html'

#class PostDetail(generic.DetailView):
#    model = models.Post
#    template_name = 'post_detail.html'



#booking meeting system



