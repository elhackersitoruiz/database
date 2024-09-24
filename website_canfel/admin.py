from django.contrib import admin
from .models import Propietario, Mascota, Veterinario, Cita, Vacuna, Desparasitacion, Cirugia
# Register your models here.

admin.site.register(Propietario)
admin.site.register(Mascota)
admin.site.register(Veterinario)
admin.site.register(Cita)
admin.site.register(Vacuna)
admin.site.register(Desparasitacion)
admin.site.register(Cirugia)
