from django.core.validators import RegexValidator
from django.db import models
from django.contrib import admin

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex='^\d{9}$', message='El teléfono debe contener 9 dígitos')]
    )
    dni = models.CharField(
        max_length=8,
        validators=[RegexValidator(regex='^\d{8}$', message='El DNI debe contener 8 dígitos')]
    )
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_aplicacion = models.DateField()
    fecha_revacunacion = models.DateField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    SEXO_OPCIONES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]

    ESPECIE_OPCIONES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]
    
    nombre = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES)
    especie = models.CharField(max_length=5, choices=ESPECIE_OPCIONES)
    color = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    talla = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    vacunas = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
    
class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex='^\d{9}$', message='El teléfono debe contener 9 dígitos')]
    )
    email = models.EmailField()

    def __str__(self):
        return self.nombre    
    
class Cita(models.Model):
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cita para {self.mascota.nombre} con {self.veterinario.nombre} el {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"

class Desparasitacion(models.Model):
    fecha_aplicacion = models.DateField()
    tipo_producto = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    proxima_desparasitacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Desparasitación de {self.mascota.nombre} el {self.fecha_aplicacion.strftime('%d/%m/%Y')}"

class Cirugia(models.Model):
    fecha_cirugia = models.DateField()
    tipo_cirugia = models.CharField(max_length=100)
    descripcion = models.TextField()
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    fecha_retiracion_puntos = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Cirugía de {self.mascota.nombre} el {self.fecha_cirugia.strftime('%d/%m/%Y')}"