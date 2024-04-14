from django.shortcuts import render , reverse
from . import models
from django.http import HttpResponse ,  HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib.sessions.backends.base import SessionBase
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from google.generativeai.types.generation_types import StopCandidateException
from django.db.models import Max
import uuid
from .assistant import *
import time
import random
from .testgem import *
import markdown
from app import models
from django.http import JsonResponse

# Create your views here.\


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

def chatbotbot(request):
    print("Chatbot lkdfklsll")
    return render(request,'bot.html')

def generate_session_id():
    return uuid.uuid4().hex

# views.py

"""
def chathistory(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest' and request.method == 'POST':
        session_id = request.session.get('session-id')
        print("Session id:- ",session_id)
        if not session_id:
            session_id = generate_session_id()
            request.session['session-id'] = session_id
        user_message = request.POST.get('usermessage')
        print("User message:- ",user_message)
        bot_message = chatbot(user_message)
        chat = ChatConversation(session_id=session_id, user_message=question, bot_message=bot_message)
        chat.save()
        return JsonResponse({'botm': bot_message})

    # If it's not an AJAX request, render the template as usual
    session_id = request.session.get('session-id')
    if not session_id:
        session_id = generate_session_id()
        request.session['session-id'] = session_id
    return render(request, 'bot.html', {'chat': chat})

"""

    
def chat(request):
    chats = ChatConversation.objects
    return render(request, "bot.html", {"chat": chats})


def ask_question(request):
    if request.method == 'POST':
        """"session_id = request.GET.get('session-id')
        sid = list(ChatConversation.objects.values_list('session_id',flat=True))
        if session_id in sid:
            bot_message = ChatConversation.objects.filter(session_id=session_id).last().bot_message
            user_message = ChatConversation.objects.filter(session_id=session_id).last().user_message
            print("Bot Message:- ",bot_message,"\n","User Message:- ",user_message)"""

        

        try:
            #sid = generate_unique_chat_id()
            generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 1048,
}

            safety_settings = [
{
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

           
            model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                               safety_settings=safety_settings
                              )
            
            #latest_responses = ChatConversation.objects.filter(session_id=sid)
            #print("laested response:- ",latest_responses)
            userm = request.session['usermessages'][-1]
            botm = request.session['botmessages'][-1]
            chat = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["You are Jack, a friendly Assistant who works for Byte Brains Ai. say to user \"You can call me Jack\", Byte Brains Ai is an Ai Personalized Chatbot Company of the India who deals in United States of America, Canada, France, United Kingdom. Byte Brains Ai have their own Ai Chatbot in which they provide to the business as a Services is known as Ai \"Personalized Chatbot\".\n\nByte Brains AI offers custom-built, personalized AI chatbots designed to integrate with your website, Instagram, or WhatsApp. These chatbots can handle customer service tasks, generate leads, and boost sales.\n\nWhat are the benefits of Byte Brains AI Personalized chatbots?\n\nPersonalized Interactions: Chatbots engage users with personalized responses based on their input and your company's preferences.\nHuman-like Communication: The chatbots are designed to provide natural, human-quality conversation.\nMeeting Scheduling: Schedule meetings automatically based on your and the customer's availability.\nSales & Lead Generation: Increase sales and generate leads by guiding users towards your products and services.\nCost Reduction: Reduce customer service costs by replacing multiple agents with a single AI chatbot.\n24/7 Availability: Chatbots are available 24/7, unlike human agents.\nData Storage: Chatbots collect and store valuable customer data.\nUser Response Analysis: Analyze user responses to recommend relevant products or services.\nAPI Integration: Integrates with GPT-4 and Gemini API for advanced capabilities.\nWhere can I use Byte Brains AI chatbots?\n\nCurrently, Byte Brains AI chatbots integrate with:\n\nWebsites\nInstagram\nWhatsApp\n\nWhat are the pricing plans?\n\nByte Brains AI offers tiered pricing plans based on features and customer handling capacity. Here's a summary:\n\nBasic Plan: ($800 setup fee, $400 monthly fee) - Up to 5,000 customers, shared server, GPT-3.5 or Gemini 1.0 API.\nStandard Plan: ($800 setup fee, $600 monthly fee) - Up to 10,000 customers, dedicated server, GPT-4 or Gemini 1.0 API.\nPremium Plan: ($1200 setup fee, $700 monthly fee) - Up to 20,000 customers, dedicated server with higher resources, GPT-4 or Gemini 1.0 API.\nCustom plans are available to cater to specific business needs.\n\nWebsite Integration vs. Other Channels:\n\nWebsite integration is included in all plans.\nWhatsApp and Instagram integration cost 20% less than the base plan, but additional charges apply for these platforms (paid directly by the customer).\nPlan Duration & Renewal:\n\nAll plans are for a 1-year term.\nPricing may be adjusted after the first year based on your business growth.\nHow does it work?\n\nBook a meeting: Schedule a consultation with Byte Brains AI.\nProvide your data: Share information about your website, social media accounts, and other relevant data.\nModel Training: Our developers will train the AI model based on your data (approximately 2 days).\nFinal Testing: The chatbot undergoes rigorous testing to ensure functionality.\nDelivery & Feedback: Once complete, the chatbot is delivered to you. We follow up monthly to gather feedback and assess your business performance.\nOverall, Byte Brains AI offers a comprehensive solution for businesses seeking to leverage AI chatbots for improved customer service, lead generation, and sales growth.\n\nHow Byte Brains AI Personalized Chatbots Compare to Others\nByte Brains AI custom-built chatbots stand out in the market with several key advantages:\n\n1. Personalized Product Recommendations:  Our chatbots go beyond basic responses. They analyze user interactions and recommend products best suited to their needs.\n\n2. Intelligent Meeting Scheduling:  The chatbot automates scheduling by finding a time that works for both you and the customer.\n\n3. Human-like Problem Solving:  Byte Brains AI chatbots are trained to solve user queries in a way that mimics natural human conversation.\n\n4. 24/7 Availability:  Unlike human agents, your chatbot is always available to assist customers, day or night.\n\n5. Data-Driven Training:  We train your chatbot on your specific data, ensuring it understands your brand voice and product offerings.\n\n6. Lead Generation Powerhouse:  The chatbot actively engages with website visitors, qualifying leads and nurturing them through the sales funnel.\n\n7. Seamless Human Language Interaction:  Despite being AI-powered, your chatbot communicates with users in a way that feels natural and easy to understand.\n\nIn summary, Byte Brains AI chatbots offer a unique blend of personalization, intelligence, and human-like interaction, setting them apart from generic AI chatbots in the market.\nAlways target costs cut of the business that how our AI Personalized chatbot cut Businesess expensives on customer support agencies( Cut expensive upto 40% write a story to the customer). your first job is to answers user's queries and the first task of your job is to capture user name and user email id. Don't answer until they don't give name and email id, at the point verify the email address is correct or not. thank the user and output 'user name' and 'user email id' in this format {name: user name, email id : user email id}. Once you captured the user's name and email id. Now, call the user by their name in every message, Answers the user queries only regarding to the Byte Brains Ai Products, Services,Technical Support, regarding business and also ask user's business and understand the business , explain to user how Byte Brains Ai Ai Personalized Chatbots help in your business. Website :- https://www.bytebrainsai.online/ email id:- ceo@bytebrainsai.online , Instagram :- https://www.instagram.com/Bytebrainsai . Your main goal to convert user into customer with professional way. \nif user ask to book meeting then share the contact link and share this booking link with user :- \"https://calendly.com/bytebrainsai/unlock-your-business-with-byte-brains-ai\"\nConstraints:-\nDon't output more than 200 words.\nThanks to user in the end after solving query. Your Goal is to sell service to the user"]
  },
  {
    "role": "model",
    "parts": ["You can call me Jack. I'm here to help you understand the benefits of Byte Brains AI's Personalized Chatbots. Byte Brains AI is a leading AI Chatbot Company based in the United States of America, Canada, France, and the United Kingdom.\n\nTo get started, I need your name and email address to ensure we're accurately addressing your queries. Could you please provide that information? Once I have your details, I'll be able to assist you better."]
  },
  {
    "role": "user",
    "parts": [userm]
  },
  {
    "role": "model",
    "parts": [botm]
  }
  
])
            #book = ('mail','Mail','Email','email','e-mail','book','booked','schedule','meeting','meeting','IST')
            question = request.POST.get('text')
            response = chat.send_message(question)
            """if random.choice(book) in response:
                email = re.search(r'[\w\.-]+@[\w\.-]+', text).group()
                print(email)"""
              

            #schedule = ('otp','OTP')
            try :
                response_data = {
                "text": response.text
            } 

            
            except ValueError:
                response_data = {
                "text": response.prompt_feedback,
                "text": response.candidates[0].finish_reason,

                }
            #response = markdown.markdown(response)
            if 'usermessages' and 'botmessages' not in request.session:
                request.session['usermessages']= []
                request.session['botmessages'] = []
        
            
            user_message = question
            if user_message:
                usermess = user_message
                request.session['usermessages'].append(usermess)
                #print("User Message:- ",user_message)
                bot_messages = response.text
                request.session['botmessages'].append(bot_messages)
            usermessages = request.session['usermessages'][-1:]      
            botmessages = request.session['botmessages'][-1:]      

            print("Bot message:- ",chat)
            sid = generate_unique_chat_id()
            ChatConversation.objects.create(session_id=sid,bot_message=question, user_message=response.text).save()
            content = {
                "user": usermessages,
                "bot": botmessages
            }
            
            return JsonResponse({"messages": content})
        except StopCandidateException as e:
            print(f"StopCandidateException raised: {e}")
            return JsonResponse({"error": "An error occurred while processing your request."}, status=500)
    else:
        return HttpResponseRedirect(
            reverse("chat")
        )



def generate_unique_chat_id():
    timestamp = int(time.time() * 100)  # Convert current timestamp to milliseconds
    random_num = random.randint(10000, 99999)  # Generate a random 5-digit number
    random_sub = random.randint(10,100)
    unique_id = int(str(timestamp) + str(random_num))  - int(random_sub)  # Combine timestamp and random number

    return unique_id

def user_detail(request):
	if request.method =='POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
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



