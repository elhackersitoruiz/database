"""
URL configuration for project_canfel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website_canfel.views import mascota_listing, mascota_by_id, vacunas_listing, create_vacunas, register_pet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascotas/', mascota_listing, name="mascota_listing"),
    path("mascota/<int:id>/", mascota_by_id, name="mascota_by_id"),
    path("vacunas/", vacunas_listing, name="vacunas_listing"),
    path('vacunas/create/', create_vacunas, name='create_vacunas'),
    path('register_pet/', register_pet, name='register_pet'),
]
