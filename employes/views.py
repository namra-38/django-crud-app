from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Employe
from .forms import EmployeForm

# Create your views here.
def employes_list(request):
    emp = Employe.objects.all()
    template_name = 'employes/list.html'
    context = {'emp': emp}
    return render(request , template_name , context)

def employe_details(request, employe_id):
    emp = Employe.objects.get(id= employe_id)
    template_name = 'employes/details.html'
    context = {'emp': emp}
    return render(request, template_name, context)

def detele_employe(request, employe_id):
    emp = Employe.objects.get(id=employe_id)
    emp.delete()
    return redirect('employes_list')

def add_employe(request):
    form = EmployeForm()

    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employes_list')
        
    template_name = 'employes/form.html'
    context = {'form': form}
    return render(request, template_name, context)

def edit_employe(request, employe_id):
    emp = Employe.objects.get(id=employe_id)
    form = EmployeForm(request.POST or None, instance=emp)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('employe_details', args=(emp.id,)))
    template_name = 'employes/update.html'
    context = {'form': form}
    return render(request, template_name, context)        

