from django.shortcuts import render

# Create your views here.
def imagestatic(request):
    return render(request,'image.html')
