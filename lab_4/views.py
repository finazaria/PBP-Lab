from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from lab_2.models import Note
from .forms import NoteForm

def index(request):
    # Load the Note model agar bisa ditampilkan nanti di html
    notes = Note.objects.all().values()
    response = {'notes' : notes}   
    # jadi nanti 'notes' ini yang kita bawa untuk jadi variable di html files kita
    return render(request, 'lab4_index.html', response)
    # Render => combines a given template dengan dictionary yang udah kita buat tadi => response

# Method to render responses dari NoteForm
def add_note(request):
    context = {}
    # NoteForm => Model Note, tapi datanya dari form
    form = NoteForm(request.POST or None, request.FILES or None)

    # Check if form data is valid
    if form.is_valid() and request.method == "POST":
        # Save the form data to model
        form.save()
        return HttpResponseRedirect("/lab-4")      # To redirect to /lab-4 after validating and saving the data

    context['form'] = form
    return render(request, 'lab4_form.html', context)
    # di render ke lab4_form.html

def note_list(request):
    notes = Note.objects.all().values()
    response = {'notes' : notes}
    return render(request, 'lab4_note_list.html', response)

