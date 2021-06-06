from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from .models import TabelBuah
from .forms import TabelBuahForm

# Create your views here.

# create views
def tambah_buah(request):
    if request.method == 'POST':
        form = TabelBuahForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'tambah_buah.html', {'form': TabelBuahForm})

# Retrieve
# 1. List View
def list_buah(request):
    context = {}
    context['buah'] = TabelBuah.objects.all()
    return render(request, 'list_buah.html', context)

# 2. Detail View
def detail_buah(request, pk):
    context = {
        'data': TabelBuah.objects.get(id = pk)
    }
    return render(request, 'detail_buah.html', context)

# Update View
def update_buah(request, pk):
    context = {}

    obj = get_object_or_404(TabelBuah, id = pk)
    form = TabelBuahForm(request.POST or None, request.FILES or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('buah:detail_buah', args=(obj.id,)))
    
    context['form'] = form
    return render(request, 'tambah_buah.html', context)

# Delete View
def delete_buah(request, pk):
    context = {}

    obj = get_object_or_404(TabelBuah, id = pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, 'delete_buah.html', context)