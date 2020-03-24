from django.shortcuts import render,redirect
from .models import *
from .contact import *
from django.contrib import messages

# Create your views here.
def home(request):

    return render(request, 'hack/index.html')

def service(request):

    return render(request, 'hack/service.html')

def about(request):

    return render(request, 'hack/about.html')

def testimonials(request):

    return render(request, 'hack/testimonials.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('firstname')
            messages.success(request, user + "'s message was sent.")
            return redirect('contact')
        else:
            messages.success(request, 'Message not sent ')
            return redirect('contact')
    context = {'form' : form}
    return render(request, 'hack/contact.html',context)

def faq(request):

    return render(request, 'hack/faq.html')