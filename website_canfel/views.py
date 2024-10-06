from django.shortcuts import render
from django.http import JsonResponse
from website_canfel.models import Mascota, Vacuna, Propietario
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def mascota_listing(request):
    #mascota_list = [dict(m) for m in Mascota.objects.all()]
    mascota_list = Mascota.objects.all()
    m_list = []
    for mascota in mascota_list:
        mascota_dict = model_to_dict(mascota)
        mascota_dict['vacunas'] = list(mascota.vacunas.values('nombre', 'descripcion', 'fecha_aplicacion', 'fecha_revacunacion'))
        m_list.append(mascota_dict)

    return JsonResponse(m_list, safe=False)

def mascota_by_id(request, id):
    mascota =  Mascota.objects.get(id=id)
    mascota_dict = model_to_dict(mascota)
    mascota_dict['vacunas'] = list(mascota.vacunas.values('nombre', 'descripcion', 'fecha_aplicacion', 'fecha_revacunacion'))
    return JsonResponse(mascota_dict, safe=False)

def vacunas_listing(request):
    #mascota_list = [dict(m) for m in Mascota.objects.all()]
    vacuna_list = list(Vacuna.objects.values())
    return JsonResponse(vacuna_list, safe=False)

@csrf_exempt
def create_vacunas(request):
    if request.method == 'POST':
        # Extract data from POST request
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_aplicacion = request.POST.get('fecha_aplicacion')
        fecha_revacunacion = request.POST.get('fecha_revacunacion')
        
        # Ensure required fields are present (you can add more validations as needed)
        if not all([nombre, descripcion, fecha_aplicacion, fecha_revacunacion]):
            return JsonResponse({'status': 'failed', 'message': 'Missing required fields'}, status=400)
        
        try:
            # Create the Vacunas object
            vacuna = Vacuna.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                fecha_aplicacion=fecha_aplicacion,
                fecha_revacunacion=fecha_revacunacion,
            )
            return JsonResponse({'status': 'success', 'message': 'Vacunas created successfully'}, status=201)
        except Exception as e:
            # Handle any unexpected errors
            return JsonResponse({'status': 'failed', 'message': str(e)}, status=500)
    
    # If it's not a POST request, return an error
    return JsonResponse({'status': 'failed', 'message': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def register_pet(request):
    if request.method == 'POST':
        # Extract data from POST request
        nombre_mascota = request.POST.get('nombreMascota')
        especie_mascota = request.POST.get('especieMascota')
        raza_mascota = request.POST.get('razaMascota')
        talla_mascota = request.POST.get('tallaMascota')
        peso_mascota = request.POST.get('pesoMascota')
        fecha_nacimiento_mascota = request.POST.get('fechaNacimientoMascota')
        color_mascota = request.POST.get('colorMascota')
        sexo_mascota = request.POST.get('sexoMascota')
        nombre_propietario = request.POST.get('nombrePropietario')
        direccion_propietario = request.POST.get('direccionPropietario')
        dni_propietario = request.POST.get('dniPropietario')
        telefono_propietario = request.POST.get('telefonoPropietario')
        
        # Ensure required fields are present (you can add more validations as needed)
        if not all([nombre_mascota, especie_mascota, raza_mascota, fecha_nacimiento_mascota, color_mascota, sexo_mascota, nombre_propietario, direccion_propietario, dni_propietario, telefono_propietario]):
            return JsonResponse({'status': 'failed', 'message': 'Missing required fields'}, status=400)
        
        try:
            # Create the Vacunas object
            mascota = Mascota.objects.create(
                nombre=nombre_mascota,
                especie=especie_mascota,
                raza=raza_mascota,
                fecha_nacimiento=fecha_nacimiento_mascota,
                color=color_mascota,
                sexo=sexo_mascota,
                talla=talla_mascota,
                peso=peso_mascota,
                propietario=Propietario.objects.create(
                    nombre=nombre_propietario,
                    direccion=direccion_propietario,
                    dni=dni_propietario,
                    telefono=telefono_propietario
                )
            )
            return JsonResponse({'status': 'success', 'message': 'Pet created successfully'}, status=201)
        except Exception as e:
            # Handle any unexpected errors
            return JsonResponse({'status': 'failed', 'message': str(e)}, status=500)
    
    # If it's not a POST request, return an error
    return JsonResponse({'status': 'failed', 'message': 'Only POST requests are allowed'}, status=405)




# Create your views here.


