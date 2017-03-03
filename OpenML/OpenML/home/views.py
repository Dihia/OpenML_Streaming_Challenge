from django.shortcuts import render

variables = {
    "title" : "Streaming Challenges"
}


# Create your views here.
def index(request):
    return render(request, 'home/index.html', variables)
