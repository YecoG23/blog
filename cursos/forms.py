from .models import Curso, Aula
from django.forms import ModelForm

class CursoForm(ModelForm):
	class Meta:
		model = Curso
		exclude = ['creado','actualizado']

class AulaForm(ModelForm):
	class Meta:
		model = Aula
		fields = ['nombre','curso','descripcion']
		# widgets = {
		# 	'curso': SelectMultiple(choices = list(Projeto.objects.all().values_list('id','nome'))),
		# }