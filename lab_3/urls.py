from django.urls import path, include
from .views import add_friend, index

# Routing
urlpatterns = [
    path('', index, name='index'),
    path('add', add_friend, name='add_friend')

]
