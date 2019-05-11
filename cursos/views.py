## FROM DJANGO NATIVE FUNCTIONS
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

## FROM MY APP
from .models import Curso, Aula
from .forms import CursoForm, AulaForm

#DEFINING GLOBAL VARIABLE FOR "SESION"
current_sesion = 4

#GENERAL TEMPLATE VIEW INDEX
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['list_cursos'] = Curso.objects.all()
        return context

## CREATE, DETAIL, LIST AND VIEW CURSO CLASS

class CursoCreateView(SuccessMessageMixin, CreateView):
	model = Curso
	success_message = 'Curso creado exitosamente!'
	form_class = CursoForm

class CursoDetailView(DetailView):
    model = Curso
    # template_name = 'cursos/curso_detail.html'
    def get_context_data(self, **kwargs):
        context = super(CursoDetailView, self).get_context_data(**kwargs)
        context['current_sesion'] = current_sesion
        context['aulas'] = Aula.objects.filter(curso__slug=self.kwargs['slug']).order_by('num_sesion')
        context['list_cursos'] = Curso.objects.all()
        return context

class CursoListView( ListView):
    model = Curso
    def get_context_data(self, **kwargs):
        context = super(CursoListView, self).get_context_data(**kwargs)
        context['list_cursos'] = Curso.objects.all()
        return context

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
    slug = None
    def get_context_data(self, **kwargs):
        context = super(AulaDetailView, self).get_context_data(**kwargs)
        curso_nombre = self.kwargs['slug']
        context['curso_nombre'] = curso_nombre
        aulas_by_current_curso = Aula.objects.filter(slug=self.kwargs['slug']).order_by('num_sesion')
        # print(self.kwargs['slug'])
        # print(aulas_by_current_curso)
        context['aulas'] = aulas_by_current_curso
        context['list_cursos'] = Curso.objects.all()
        
        return context

class AulaListView( ListView):
    model = Aula

class AulaUpdateView(SuccessMessageMixin, UpdateView):
    model = Aula
    success_message = 'Aula actualizada con exito!'
    form_class = CursoForm

class AulaDeleteView(DeleteView):
    model = Aula
    success_url = reverse_lazy('list_aulas')
