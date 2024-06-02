from django.shortcuts import render
from django.http import HttpResponse

from homescreen.models import ToDo
# Create your views here.
def home(request):
    all = ToDo.objects.all()
    info = {'todos': all}
    return render(request, 'home.html', context=info)