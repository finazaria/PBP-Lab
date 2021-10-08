from django.urls import path, include
from .views import index, add_note, note_list

# Routing
urlpatterns = [
    # path utama
    path('', index, name='index'),   # /lab-4  
    path('add-note', add_note, name='add_note'),     # /lab-4/add-note
    path('note-list', note_list, name='note_list')     # lab-4/note-list
]
