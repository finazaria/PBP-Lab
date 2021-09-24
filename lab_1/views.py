from django.shortcuts import render
from datetime import datetime, date
from .models import Friend              # Model friend harus diimport terlebih dahulu
                                        # agar bisa dipanggil di bawah

mhs_name = 'Alfina Azaria'  # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(2002, 8, 20)  # TODO Implement this, format (Year, Month, Date)
npm = 2006482773 # TODO Implement this

# ini untuk ngelink ke files html nya
def index(request):
    response = {'name': mhs_name,
                'age': calculate_age(birth_date.year),
                'npm': npm}
    return render(request, 'index_lab1.html', response) # masukin sesuai nama file html nya


def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0

# kita harus memanggil model friend di views.py
def friend_list(request):       # sama kayak def index(request) di slide kelas
    friends = Friend.objects.all().values() # TODO Implement this
    response = {'friends': friends}          # To save the responds
    return render(request, 'friend_list_lab1.html', response)
