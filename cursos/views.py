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

#DEFINING GLOBAL VARIABLE FOR "SESION"
current_sesion = 4

## CREATE, DETAIL, LIST AND VIEW CURSO CLASS

class CursoCreateView(SuccessMessageMixin, CreateView):
	model = Curso
	success_message = 'Curso creado exitosamente!'
	form_class = CursoForm

class CursoDetailView(DetailView):
    model = Curso
    def get_context_data(self, **kwargs):
        context = super(CursoDetailView, self).get_context_data(**kwargs)
        context['current_sesion'] = current_sesion
        context['aulas'] = Aula.objects.filter(curso__id=self.kwargs['pk'])
        return context

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
    template_name = 'cursos/curso_aula_detail.html'

class AulaListView( ListView):
    model = Aula

class AulaUpdateView(SuccessMessageMixin, UpdateView):
    model = Aula
    success_message = 'Aula actualizada con exito!'
    form_class = CursoForm

class AulaDeleteView(DeleteView):
    model = Aula
    success_url = reverse_lazy('list_aulas')
