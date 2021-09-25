from django.urls import path, include
from .views import index
from .views import xml
from .views import json

# Routing
urlpatterns = [
    # path utama
    path('', index, name='index'),     
    # Routing index dari views agar bisa dimunculkan di website

    # path XML
    path('xml', xml, name = 'xml'),

    # path JSON
    path('json', json, name = 'json')
]
