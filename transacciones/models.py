from django.db import models

# Create your models here.
TIPOS  = (
    ('i', 'Ingreso'),
    ('g', 'Gasto'),
)
class Categoria(models.Model):
    """Model definition for Categoria."""

    nombre = models.CharField(max_length=50)
    tipo = models.CharField(choices = TIPOS, max_length=1)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre



class Transaccion(models.Model):
    """Model definition for Transaccion."""
    titulo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    detalle = models.TextField(blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField(auto_now=True, auto_now_add=False)
    tipo = models.CharField(choices = TIPOS, max_length=1)



    class Meta:
        """Meta definition for Transaccion."""

        verbose_name = 'Transaccion'
        verbose_name_plural = 'Transaccions'

    def __str__(self):
        """Unicode representation of Transaccion."""
        return f'{self. titulo}: {self.valor}'
