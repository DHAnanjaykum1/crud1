from statistics import mode
from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,FormView,CreateView
# Create your views here.
from .models import Contact

class HomeView(ListView):
    model = Contact
    paginate_by= 2

class InsertView(CreateView):
    model = Contact
    fields = ["name","contact","email","city"]
    success_url = reverse_lazy("homepage")

class RemoveView(DeleteView):
    model = Contact
    success_url = reverse_lazy("homepage")

class EditView(UpdateView):
    model = Contact
    fields = ["name","contact","email","city"]
    success_url = reverse_lazy("homepage")
