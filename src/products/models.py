from django.db import models


# Create your models here.
class Product(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)

    # newly added field, but django doesn't know. so we need to add something to tell django
    featured = models.BooleanField(default=False)  # null=True or default=True
