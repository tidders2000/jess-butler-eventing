from django.db import models

# Create your models here.

class signup (models.Model):
    name = models.CharField(max_length=254, default='')
    email= models.EmailField(max_length=254)
    optout= models.BooleanField(default=False)
    def __str__(self):
        return self.name