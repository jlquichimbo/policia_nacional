from django.db import models

# Create your models here.
class Persona(models.Model):
    """Modelo de datos para persona."""
    TIPOS_SANGRE = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-')
    )
    RANGOS =  (
        ('1','Capitán'),
        ('2','Teniente'),
        ('3','Subteniente'),
        ('4','Sargento Primero'),
        ('5','Sargento Segundo'),
        ('6','Cabo Primero'),
        ('7','Cabo Segundo'),
    )

    identificacion = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    tipo_sangre = models.CharField(choices=TIPOS_SANGRE, max_length=3)
    ciudad_nacimiento = models.CharField(max_length=50)
    telefono_celular = models.CharField(max_length=10)
    rango_grado = models.CharField(choices=RANGOS, max_length=1)
    dependencia = models.CharField(max_length=50)


    

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of Persona."""
        return f'{self.rango_grado}. {self.apellidos}'
