from django.shortcuts import render
from . import models
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def sw(request):
	return render(request,'sw.js')

def sitemap(request):
	return render(request,'sitemap.xml')

def Ads(request):
	return render(request,'Ads.txt')

def robots(request):
	return render(request,'Robots.txt')

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

def user_detail(request):
	if request.method =='POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['subject']
		query = models.query(name=name, email=email,subject=subject,message=message)
		query.save()
		return render(request,'contact.html',{'query':"Thanks for Contacting, We will back to you as soon as possible."})

def blog(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request,'blog.html',context)
    #return render(request,'blog.html')

def chatbot(request):
    return render(request,'Ai chatbo.html')



def post(request,slug):
    postonly = Post.objects.filter(slug=slug).first()
    context = {'postonly': postonly}
    return render(request,'blogbase.html',context)
#class PostList(generic.ListView):
#    queryset = models.Post.objects.filter(status=1).order_by('-created_on')
#    template_name = 'blog.html'

#class PostDetail(generic.DetailView):
#    model = models.Post
#    template_name = 'post_detail.html'



#booking meeting system



