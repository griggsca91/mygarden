from django.shortcuts import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse(b"{\"text\": \"Hello, world. You're at the polls index.\"}", content_type="text/json")
