from django.contrib import admin

# Register Note model di admin, agar bisa diakses dari Django Admin

from .models import Note
admin.site.register(Note)
