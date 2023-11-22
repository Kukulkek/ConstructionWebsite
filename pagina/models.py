from django.db import models

# Create your models here.
class Material(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    CHOICES = [
        ('option1', 'Metro Cuadrado'),
        ('option2', 'Metro Cubico'),
        ('option3', 'Kilo'),
        ('option4', 'Unidad'),
    ]
    medida = models.CharField(max_length=20, choices=CHOICES, verbose_name='Medida')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion')
    imagen = models.ImageField(upload_to='img/uploads', null=True, verbose_name='Imagen')

    def __str__(self):
        fila = "Nombre: " + self.nombre
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    session_key = models.CharField(max_length=255, unique=True)
    materials = models.ManyToManyField(Material, through='CartMaterial')

class CartMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

