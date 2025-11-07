from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Jugador, Partido

# ==========================================
# VISTA DE INICIO
# ==========================================
def inicio_futbol(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS PARA EQUIPO
# ==========================================
def agregar_equipo(request):
    if request.method == 'POST':
        Equipo.objects.create(
            nombre=request.POST['nombre'],
            ciudad=request.POST['ciudad'],
            pais=request.POST['pais'],
            fundacion=request.POST['fundacion'],
            estadio=request.POST['estadio'],
            entrenador=request.POST['entrenador'],
            colores=request.POST['colores']
        )
        return redirect('ver_equipos')
    return render(request, 'equipo/agregar_equipo.html')

def ver_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipo/ver_equipos.html', {'equipos': equipos})

def actualizar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    return render(request, 'equipo/actualizar_equipo.html', {'equipo': equipo})

def realizar_actualizacion_equipo(request, id):
    if request.method == 'POST':
        equipo = get_object_or_404(Equipo, id=id)
        equipo.nombre = request.POST['nombre']
        equipo.ciudad = request.POST['ciudad']
        equipo.pais = request.POST['pais']
        equipo.fundacion = request.POST['fundacion']
        equipo.estadio = request.POST['estadio']
        equipo.entrenador = request.POST['entrenador']
        equipo.colores = request.POST['colores']
        equipo.save()
        return redirect('ver_equipos')
    return redirect('ver_equipos')

def borrar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    return render(request, 'equipo/borrar_equipo.html', {'equipo': equipo})

def realizar_borrado_equipo(request, id):
    if request.method == 'POST':
        equipo = get_object_or_404(Equipo, id=id)
        equipo.delete()
        return redirect('ver_equipos')
    return redirect('ver_equipos')

# ==========================================
# VISTAS PARA JUGADOR
# ==========================================
def agregar_jugador(request):
    equipos = Equipo.objects.all()
    if request.method == 'POST':
        equipo = get_object_or_404(Equipo, id=request.POST['equipo'])
        Jugador.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            fecha_nacimiento=request.POST['fecha_nacimiento'],
            nacionalidad=request.POST['nacionalidad'],
            posicion=request.POST['posicion'],
            numero_camiseta=request.POST['numero_camiseta'],
            equipo=equipo
        )
        return redirect('ver_jugadores')
    return render(request, 'jugador/agregar_jugador.html', {'equipos': equipos})

def ver_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugador/ver_jugadores.html', {'jugadores': jugadores})

def actualizar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    equipos = Equipo.objects.all()
    return render(request, 'jugador/actualizar_jugador.html', {'jugador': jugador, 'equipos': equipos})

def realizar_actualizacion_jugador(request, id):
    if request.method == 'POST':
        jugador = get_object_or_404(Jugador, id=id)
        equipo = get_object_or_404(Equipo, id=request.POST['equipo'])
        jugador.nombre = request.POST['nombre']
        jugador.apellido = request.POST['apellido']
        jugador.fecha_nacimiento = request.POST['fecha_nacimiento']
        jugador.nacionalidad = request.POST['nacionalidad']
        jugador.posicion = request.POST['posicion']
        jugador.numero_camiseta = request.POST['numero_camiseta']
        jugador.equipo = equipo
        jugador.save()
        return redirect('ver_jugadores')
    return redirect('ver_jugadores')

def borrar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    return render(request, 'jugador/borrar_jugador.html', {'jugador': jugador})

def realizar_borrado_jugador(request, id):
    if request.method == 'POST':
        jugador = get_object_or_404(Jugador, id=id)
        jugador.delete()
        return redirect('ver_jugadores')
    return redirect('ver_jugadores')