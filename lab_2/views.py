# Views is the bridge from database to template
# from models to template
from django.http import response
from django.shortcuts import render
from .models import Note
from django.http.response import HttpResponse
from django.core import serializers

# Create index method to render the HTML files
def index(request):
    # Load the Note model agar bisa ditampilkan nanti di html
    notes = Note.objects.all().values()
    response = {'notes' : notes}             # Harus dictionary 
    # jadi nanti 'notes' ini yang kita bawa untuk jadi variable di html files kita
    return render(request, 'lab2.html', response)

# Creating XML method to render XML for our response
# fungsinya sama kyk html di atas, cuma ini untuk XML 
def xml(request):
    # Load the Note model agar bisa ditampilkan nanti di html
    data = serializers.serialize('xml', Note.objects.all())
    return HttpResponse(data, content_type="application/xml")

def json(request):
    data = serializers.serialize('json', Note.objects.all())
    return HttpResponse(data, content_type="application/json")