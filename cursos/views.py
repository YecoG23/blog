## FROM DJANGO NATIVE FUNCTIONS
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

## FROM MY APP
from .models import Curso, Aula
from .forms import CursoForm, AulaForm

## CREATE, DETAIL, LIST AND VIEW CURSO CLASS

class CursoCreateView(SuccessMessageMixin, CreateView):
	model = Curso
	success_message = 'Curso creado exitosamente!'
	form_class = CursoForm

class CursoDetailView(DetailView):
    model = Curso

class CursoListView( ListView):
    model = Curso

class CursoUpdateView(SuccessMessageMixin, UpdateView):
    model = Curso
    success_message = 'Curso actualizado con exito!'
    form_class = CursoForm

class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy('list_cursos')

## CREATE, DETAIL, LIST AND VIEW AULA CLASS

class AulaCreateView(SuccessMessageMixin, CreateView):
	model = Aula
	success_message = 'Aula creado exitosamente!'
	form_class = Aula

class AulaDetailView(DetailView):
    model = Aula

class AulaListView( ListView):
    model = Aula

class AulaUpdateView(SuccessMessageMixin, UpdateView):
    model = Aula
    success_message = 'Aula actualizada con exito!'
    form_class = CursoForm

class AulaDeleteView(DeleteView):
    model = Aula
    success_url = reverse_lazy('list_aulas')
