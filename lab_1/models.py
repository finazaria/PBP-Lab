from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility

# TODO Create Friend model that contains name, npm, and DOB (date of birth) here


class Friend(models.Model):
    name = models.CharField(max_length=30)
    # TODO Implement missing attributes in Friend model
    npm = models.IntegerField()
    dob = models.DateField()        # coba gini dulu, kalo error baru coba lagi
    
# Masih bisa ditambah2in another class.
