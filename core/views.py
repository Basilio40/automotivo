from django.http import response
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .models import Marca, Automotivo,Person
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html' )

def formulario(request):

    marcas = Marca.objects.all()
    variaveis = { 
        'marcas': marcas
    }

    if request.POST:
        auto = Automotivo()
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.ano = request.POST.get('txtAno')
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.marca = marca

        try:
            auto.save()
            variaveis['mensagem'] = 'Salvo com Sucesso !!!!'
        except:
            variaveis['mensagem'] = ' Não possivel Salvar '


    return render(request, 'core/formulario.html', variaveis)

# CRUD de automoveis

def lista_automoveis(request):

    autos = Automotivo.objects.all()

    return render(request, 'core/lista_automoveis.html', {'autos':autos})

def eliminar_auto(request, id):
    # buscar automov que deseja excluir
    auto = Automotivo.objects.get(id = id)

    try:
        auto.delete()
        mensagem =  "Eliminado com sucesso !"
        messages.success(request, mensagem)
    except:
        mensagem = "Não possivel eliminar"
        messages.error(request, mensagem)

    return redirect('lista_autos')

def modificar_auto(request,id):
    # buscar automovel para modificar

    auto = Automotivo.objects.get(id = id)
    marcas = Marca.objects.all()
    variaveis = {'auto':auto, 'marcas':marcas}

    if request.POST:
        auto = Automotivo()
        auto.id = request.POST.get('txtId')
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.ano = request.POST.get('txtAno')
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.marca = marca

        try:
            auto.save()
            messages.success(request,"modificado com sucesso !!")
        except:
            messages.error(request, 'Impossivel Modificar')
        return redirect('lista_autos')


 
    return render(request, 'core/modificar_auto.html', variaveis)



class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')

def teste(request):

    return render(request, 'core/teste.html')


    