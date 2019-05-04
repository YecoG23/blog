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
    re_path('lista', CursoListView.as_view(), name='list_cursos'),
    re_path(r'^add$', CursoCreateView.as_view(), name='new_curso'),
    re_path(r'^(?P<pk>[0-9]+)/detail$', CursoDetailView.as_view(), name='view_curso'),
    re_path(r'^(?P<pk>[0-9]+)/edit$', CursoUpdateView.as_view(), name='edit_curso'),
    re_path(r'^(?P<pk>[0-9]+)/delete$', CursoDeleteView.as_view(), name='delete_curso'),
]