from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'ninja_gold/index.html')
