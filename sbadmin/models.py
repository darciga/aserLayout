from django.db import models

# Create your models here.
class servicio(models.Model):
	entrada = models.DateField(verbose_name = 'Fecha de entrada',auto_now = False)
	folio = models.CharField(verbose_name='Numero de folio', max_length=5)
	estado = models.CharField(verbose_name='Estado actual del servicio', max_length=20)
	tecnico = models.CharField(verbose_name='Nombre del tecnico', max_length=80)
	equipo = models.TextField(verbose_name='Descripcion del equipo')
	cliente = models.CharField(verbose_name='Nombre del cliente',max_length=80)

	def __unicode__(self):
		return self.folio
