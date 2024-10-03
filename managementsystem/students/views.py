from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from students.models import Student
from django.urls import reverse_lazy

# Create your views here.

class HomePage(ListView):
    model= Student
    template_name="students/index.html"

class CreatePage(CreateView):
    model= Student
    fields=["first_name", "last_name","date_of_birth", "email", "phone_number", "mat_number", "gender"]
    template_name="students/create.html"

class UpdatePage(UpdateView):
    model= Student
    fields=["first_name", "last_name","date_of_birth", "phone_number", "gender"]
    success_url = reverse_lazy("home")
    template_name="students/update.html"

class DeletePage(DeleteView):
    model= Student
    success_url = reverse_lazy("home")
    template_name="students/delete.html"