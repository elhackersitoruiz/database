from django.shortcuts import render
from django.http import JsonResponse
from website_canfel.models import Mascota
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404


def mascota_listing(request):
    #mascota_list = [dict(m) for m in Mascota.objects.all()]
    mascota_list = list(Mascota.objects.values())
    return JsonResponse(mascota_list, safe=False)

def mascota_by_id(request, id):
    mascota =  model_to_dict(Mascota.objects.get(id=id))
    return JsonResponse(mascota, safe=False)


# Create your views here.


