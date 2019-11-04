from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_to_polls(request):
    # redirect uer to the polls index
    return HttpResponseRedirect(reverse('polls:index'))
