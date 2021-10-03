from django.db import models

# Create a Note model
class Note(models.Model):
    to = models.CharField(max_length=30)
    From = models.CharField(max_length=30)     # soalnya 'from' doang merupakan suatu perintah default
                                                # jadi kita pake From untuk membedakan
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    
