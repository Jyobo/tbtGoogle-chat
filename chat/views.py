# Create your views here.

from chat.models import Message
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime

class valid_form():
      if form.is_valid():
            m = form.save(commit=False)
            m.user = request.user
            m.save()
            return HttpResponseRedirect('/chat/')     
        else:
            form = MessageForm()
            return render_to_response('base.html', {'form':form }, context_instance=RequestContext(request))
     

        

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['user']


@login_required
def base(request):
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        valid_form()


@login_required
def messages(request):
    messages = Message.objects.all()[:10]
    return render_to_response('messages.html', {'messages': messages})
