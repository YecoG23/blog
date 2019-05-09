from django.urls import path, re_path
from .views import (
    CursoCreateView,
    CursoDetailView,
    CursoListView,
    CursoUpdateView,
    CursoDeleteView,
    AulaCreateView,
    AulaDetailView,
    AulaListView,
    AulaUpdateView,
    AulaDeleteView,
)

urlpatterns = [
    # urls for cursos
    re_path('lista', CursoListView.as_view(), name='list_cursos'),
    re_path(r'^add$', CursoCreateView.as_view(), name='new_curso'),
    path('<int:pk>/detail', CursoDetailView.as_view(), name='view_curso'),
    re_path(r'^(?P<pk>[0-9]+)/edit$', CursoUpdateView.as_view(), name='edit_curso'),
    re_path(r'^(?P<pk>[0-9]+)/delete$', CursoDeleteView.as_view(), name='delete_curso'),
    # urls for aulas
    path('<slug:slug>/lista_aulas', AulaListView.as_view(), name='list_aulas'),
    path('<slug:slug>/add', AulaCreateView.as_view(), name='new_aula'),
    path('<slug:slug>/<int:id>/detail', AulaDetailView.as_view(), name='view_aula'),
    path('<slug:slug>/<int:id>/edit', AulaUpdateView.as_view(), name='edit_aula'),
    path('<slug:slug>/<int:id>/delete', AulaDeleteView.as_view(), name='delete_aula'),
]