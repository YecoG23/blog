from django.db import models
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.

User = settings.AUTH_USER_MODEL

class Curso(models.Model):

	profesor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	#asistente = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120, blank=True)
	descripcion = models.TextField(null=True, blank=True)
	banner_img = models.ImageField(upload_to='img/', blank=True, null=True)
	programa = models.CharField(max_length=120, blank=True)
	pre_requisito = models.CharField(max_length=120, blank=True, verbose_name='Pre requisitos')
	num_credito = models.PositiveIntegerField(blank=True, verbose_name='Numero de creditos')
	ciclo_academico = models.CharField(max_length=120, blank=True, verbose_name='Ciclo academico')
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
	    self.nombre = self.nombre.lower()
	    return super(Curso, self).save(*args, **kwargs)
	    
	def get_absolute_url(self):
		return reverse('view_curso', args=[str(self.id)])

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['-nombre']

class Aula(models.Model):
	curso = models.ForeignKey(Curso, default=1, null=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=120)
	descripcion = models.TextField(null=True, blank=True)
	slug = models.SlugField(max_length=120, blank=True)
	num_sesion = models.PositiveIntegerField(blank=True)
	archivos = models.FileField(upload_to='uploads/', blank=True, null=True)
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)
	# publicado_en = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.curso.nombre)
	    super(Aula, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('view_aula', args=[str(self.id)])

	def __str__(self):
		return '{:.3}-{}'.format(self.curso.nombre,self.nombre)

	class Meta:
		ordering = ['creado','actualizado']

