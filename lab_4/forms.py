# import form class from django
from django import forms

# import Note model from lab_2 folder
from lab_2.models import Note

# Create a ModelForm
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"