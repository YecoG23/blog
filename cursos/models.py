from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Curso(models.Model):

	profesor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	#asistente = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=120)
	descripcion = models.TextField(null=True, blank=True)
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('view_curso', args=[str(self.id)])

	def __str__():
		return self.nombre

	class Meta:
		ordering = ['-nombre']

class Aula(models.Model):
	curso = models.ForeignKey(Curso, default=1, null=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=120)
	## archivos = FileField(upload_to='uploads/')
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)
	publicado_en = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('view_aula', args=[str(self.id)])

	def __str__():
		return self.nombre

	class Meta:
		ordering = ['publicado_en','actualizado','creado']