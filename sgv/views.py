from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Visitors, AccessSEDE
from .forms import AccessSEDEForm, VisitanteForms, SearchForm
from django.utils import timezone




######################################################################3
#
######################################################################
def Dashboard(request):
    return render(request, 'index.html')

def add_visitor(request):
    if request.method == "POST":
        form = VisitanteForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_visitantes')
    else:
        form = VisitanteForms()
    return render(request, 'crear_visitante.html', {'form': form})

def papelera(request):
    visitors = Visitors.objects.filter(is_deleted=True)
    return render(request, 'papelera_reciclaje.html', {'visitors': visitors})



def detalleVisitante(request, dni):
    visitor = get_object_or_404(Visitors, Dni=dni)
    # Filtrar los accesos por el día actual
    accesses_today = AccessSEDE.objects.filter(visitor=visitor).order_by('entry', 'hours')
    #accesses_today = AccessSEDE.objects.filter(visitor=visitor)
    return render(request, 'detalle_visitante.html', {'visitor': visitor, 'accesses_today': accesses_today})





def delete_restore_visitor(request, dni):
    visitor = get_object_or_404(Visitors, Dni=dni)    
    action_text = 'Restaurar' if visitor.is_deleted else 'Eliminar'
    if request.method == 'POST':
        if 'delete' in request.POST:
            visitor.is_deleted = True
        elif 'restore' in request.POST:
            visitor.is_deleted = False
        visitor.save()
        return redirect('lista_visitantes')  # Cambia esto a la URL deseada
    return render(request, 'confirmar_borrado.html', {'visitor': visitor, 'action_text': action_text})

def edit_visitor(request, dni):
    visitor = get_object_or_404(Visitors, Dni=dni)
    if request.method == 'POST':
        form = VisitanteForms(request.POST, request.FILES, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('detalle_visitante', dni=dni)
    else:
        form = VisitanteForms(instance=visitor)
    
    return render(request, 'edit_visitor.html', {'form': form, 'visitor':visitor})

def Listado_Filtro_Buscar(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            try:
                visitor = Visitors.objects.get(Dni=dni)
                return redirect('detalle_visitante', visitor)
            except Visitors.DoesNotExist:
                return redirect('crear_visitante')
    else:
        form = SearchForm()
    
    visitors = Visitors.objects.filter(is_deleted=False)
    return render(request, 'listado_de_visitante.html', {'visitors': visitors, 'form': form})




from django.http import HttpResponse

def favicon(request):
    return HttpResponse(status=204)


def add_access(request, visitor_id):
    visitor = get_object_or_404(Visitors, pk=visitor_id)
    if request.method == "POST":
        form = AccessSEDEForm(request.POST)
        if form.is_valid():
            access = form.save(commit=False)
            now = timezone.localtime()
            # Verificar si la fecha y hora del acceso son iguales a la fecha y hora actuales
            if access.entry == now.date():
                access.visitor = visitor
                access.save()
                return redirect('detalle_visitante', dni=visitor.Dni)
            else:
                form.add_error(None, 'La fecha y la hora del acceso deben ser las actuales.')
    else:
        form = AccessSEDEForm()
    return render(request, 'add_access.html', {'form': form, 'visitor': visitor})