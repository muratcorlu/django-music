from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render_to_response('music/home.html', {}, context_instance=RequestContext(request))