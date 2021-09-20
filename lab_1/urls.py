from django.urls import path, include
from .views import friend_list, index
# from .views import 

# Routing
urlpatterns = [
    path('', index, name='index'),
    # TODO Add friends path using friend_list Views
    path('friends', friend_list, name = 'friends')     

]
