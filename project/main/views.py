from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def whyweloveyou(req):
    return render(req, 'love.html')

def poem(req):
    return render(req, 'poem.html')