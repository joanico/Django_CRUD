from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'application_form/index.html')


class ContactList(ListView):
    model = Contact


class ContactDetail(DetailView): 
    model = Contact


class ContactCreate(CreateView): 
    model = Contact
    fields = ['name', 'email', 'address', 'phone']
    success_url = '/'


class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name', 'email', 'address', 'phone']
    success_url = '/'


class ContactDelete(DeleteView): 
    model = Contact
    success_url = '/'
