from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from lab_1.models import Friend
from lab_3.forms import FriendForm

# ini tampilan friends biasa
@login_required(login_url='/admin/login/')
def index(request):
    friends = Friend.objects.all().values() 
    response = {'friends': friends}          # To save the responds
    return render(request, 'lab3_index.html', response)

# Method to create Friend with data from the Form
# To render the form and save the data directly to the database
@login_required(login_url='/admin/login/')
def add_friend(request):
    context = {}

    # create object of form
    # Friendform => kayak model Friend, tapi yang dari form
    form = FriendForm(request.POST or None, request.FILES or None)

    # Check if form data is valid
    if form.is_valid() and request.method == "POST":
        # Save the form data to model
        form.save()
        return HttpResponseRedirect("/lab-3")      # To redirect to /lab-3 after validating and saving the data

    context['form'] = form
    return render(request, 'lab3_form.html', context)
