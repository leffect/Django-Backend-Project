from django.db import models

# Create your models here.
class serve77(models.Model):
    nameserve = models.CharField(max_length=400, blank=False)
    description = models.TextField(max_length=800, blank=False)
    iconboxc = models.TextField(max_length=800, blank=False)
    dcode = models.TextField(max_length=800, blank=False)
    icondx = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.nameserve
