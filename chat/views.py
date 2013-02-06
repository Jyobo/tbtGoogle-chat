from django.http import HttpResponse
from chat.models import Message
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime

def hello(request):
    return HttpResponse("Hello world")
    
def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('login.html',{'state':state, 'username': username})
    
        

class MessageForm(ModelForm):
	class Meta:
		model = Message
		exclude = ['user']


# @login_required
def base(request):
	if request.method == "POST":
		form = MessageForm(data=request.POST)
		valid_form()


# @login_required
def messages(request):
	messages = Message.objects.all()[:10]
	return render_to_response('messages.html', {'messages': messages})
