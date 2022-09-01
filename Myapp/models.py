from django.db import models

# Create your models here.
# class Contact (models.Model):

#     name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
#     phone = models.CharField(max_length=200)
#     message = models.CharField(max_length=200)

# pass means pause


# Create your models here.

class Contact(models.Model) :

    def __str__(self):
        return self.name
    name = models.CharField(max_length= 200)
    email = models.EmailField(max_length =200)
    phone = models.IntegerField()
    message = models.TextField(max_length = 200)


