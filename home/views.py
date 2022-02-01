from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        Contact.save()
        message.success("Your message has been sent.")
    return render(request,'index.html')
