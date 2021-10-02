# import form class from django
from django import forms

# import Friend model from lab_1 folder
from lab_1.models import Friend

# Create a ModelForm
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = "__all__"