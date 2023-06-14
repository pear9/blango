from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])