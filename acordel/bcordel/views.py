from django.shortcuts import render
from .import views
# Create your views here.
def CordelView(request):
    return render(request, 'bcordel/cordel.html')
