from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Nota
from .forms import NotaForm
# Create your views here.


def listar_notas_user(request):
    notas = Nota.objects.filter(autor=request.user.pk)

    return render(request,'notas/notas_list_view.html',
            {
                'notas':notas,
                'form':NotaForm
            })

def create_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        
        if form.is_valid():
            nota = form.save(commit=False)
            nota.autor = request.user 
            nota.save()
            print(nota)

            return redirect(reverse('notas:listar_notas_user'))
    
    return redirect(reverse('notas:listar_notas_user'))

def update_nota(request,pk):
    nota = Nota.objects.filter(pk=pk).first()
    
    if request.method == 'POST':
        new_form = NotaForm(request.POST,instance=nota)
        if new_form.is_valid():
            new_form.save()
            
            return redirect(reverse('notas:listar_notas_user')) 
    else:
        form = NotaForm(instance=nota)

    return render(request,'notas/nota_update_view.html',{
        'form':form,
        'nota':nota
    })

def delete_nota(request,pk):
    nota = Nota.objects.filter(pk=pk).first()
    if request.method == 'POST':
        nota.delete()
        return redirect(reverse('notas:listar_notas_user'))
        
    return render(request,'notas/nota_delete_view.html',{'nota':nota})
