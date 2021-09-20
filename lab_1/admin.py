from django.contrib import admin

# TODO Register Friend model here
# Liat di slide kelas
from .models import Friend
admin.site.register(Friend)     # untuk register friend ke dashboard. Agar juga bisa memasukan data

