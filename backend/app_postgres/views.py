from django.shortcuts import render, redirect, get_object_or_404
from .models import TablaPostgres
from django.http import HttpResponse

# Listar registros
def listar_registros(request):
    registros = TablaPostgres.objects.all()
    return render(request, 'app_postgres/listar_registros.html', {'registros': registros})

# Crear un nuevo registro
def crear_registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        TablaPostgres.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('listar_registros')
    return render(request, 'app_postgres/crear_registro.html')

# Editar un registro
def editar_registro(request, id):
    registro = get_object_or_404(TablaPostgres, id=id)
    if request.method == 'POST':
        registro.nombre = request.POST.get('nombre')
        registro.descripcion = request.POST.get('descripcion')
        registro.save()
        return redirect('listar_registros')
    return render(request, 'app_postgres/editar_registro.html', {'registro': registro})

# Eliminar un registro
def eliminar_registro(request, id):
    registro = get_object_or_404(TablaPostgres, id=id)
    registro.delete()
    return redirect('listar_registros')
