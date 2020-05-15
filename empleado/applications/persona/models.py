from django.db import models
#
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

# Create your models here.
class Empleado(models.Model):
    
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    #contador
    #administrador
    #economista
    #otro
    fisrt_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('nombres completos', max_length=50, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True) 
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering=['fisrt_name', 'last_name']
        unique_together = ('fisrt_name', 'departamento') 
    
    def __str__(self):
        return str(self.id) + '-' + self.fisrt_name + '-' + self.last_name