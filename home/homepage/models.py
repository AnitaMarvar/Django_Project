from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
#     return self.name  to change the name of the object in db