from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

# Create your models here.

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de Modificacion', auto_now=True)
    deleted_at = models.DateTimeField('Fecha de Eliminacion', null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_deleted = models.BooleanField('Eliminado', default=False)  # Campo para el borrado lógico

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.deleted_by = kwargs.get('deleted_by', None)  # Agregado para pasar el usuario que está eliminando
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.deleted_by = None
        self.save()


def visitor_photo_upload_path(instance, filename):
    # Construir la ruta de la carpeta usando el DNI del visitante
    dni_folder = str(instance.Dni)
    return os.path.join('Photo', dni_folder, filename)


class Visitors(ModeloBase):
    LIST_NAC = [
        ('VE', 'VENEZOLANO'),
        ('EX', 'EXTRANJERO'),
    ]
    Nac = models.CharField('Nacionalidad', max_length=2, choices=LIST_NAC, default='VE')
    Dni = models.CharField('Cedula', max_length=10, unique=True)
    First_name = models.CharField('Nombre', max_length=40)
    Last_name = models.CharField('Apellido', max_length=40)
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    gender = models.CharField('Género', max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    photo = models.ImageField('Fotografía', upload_to=visitor_photo_upload_path, default='Photo/default.jpg')

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        ordering = ['Dni']

    def __str__(self):
        return self.Dni


class AccessSEDE(models.Model):
    visitor = models.ForeignKey(Visitors, on_delete=models.CASCADE, related_name='accesses')
    entry = models.DateField('Fecha del Dia')
    hours = models.TimeField('Hora de Entrada')
    hoursEx = models.TimeField('Hora de Salida', null=True, blank=True)
    TYPE_VEHICLE = [
        ('NONE', 'NO POSEE'),
        ('SEDANES', 'CARRO LIVIANO-(TIPO SEDAN)'),
        ('CARGA', 'CAMION'),
    ]
    Automovils = models.CharField('tipo de Automovil', max_length=8, choices=TYPE_VEHICLE, default='NONE')
    Licenses = models.CharField('Placa del Vehiculo', max_length=10, null=True, blank=True)
    obs = models.TextField('Observaciones', max_length=140, null=True, blank=True)

    class Meta:
        verbose_name = "Listado Accesos"
        verbose_name_plural = "Listado Accesos"

        ordering = ['entry', 'hours']

    def __str__(self):
        return f"{self.visitor.Dni} {self.entry} {self.hours}"
 
