from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Diplom
from .forms import DiplomForm

def diplom_list(request):
    diploms = Diplom.objects.all()
    return render(request, 'diploms/diplom_list.html', {'diploms': diploms})

def diplom_create(request):
    if request.method == 'POST':
        form = DiplomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diplom_list')
    else:
        form = DiplomForm()
    return render(request, 'diploms/diplom_form.html', {'form': form})

def diplom_edit(request, pk):
    diplom = get_object_or_404(Diplom, pk=pk)
    if request.method == 'POST':
        form = DiplomForm(request.POST, instance=diplom)
        if form.is_valid():
            form.save()
            return redirect('diplom_list')
    else:
        form = DiplomForm(instance=diplom)
    return render(request, 'diploms/diplom_form.html', {'form': form})
