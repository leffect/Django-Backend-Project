from django.db import models

# Create your models here.

class about(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)
    def __str__(self):
        return self.title

class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)
    def __str__(self):
        return self.title

class client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)
    def __str__(self):
        return self.name

class service6(models.Model):
    servicename = models.CharField(max_length=400, blank=False)
    description = models.TextField(max_length=800, blank=False)

    def __str__(self):
        return self.servicename

class projectview(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='projectview/', blank=False)
    def __str__(self):
        return self.name

class mega67(models.Model):
    nameserve = models.CharField(max_length=400, blank=False)
    description = models.TextField(max_length=800, blank=False)
    iconboxc = models.TextField(max_length=800, blank=False)
    dcode = models.TextField(max_length=800, blank=False)
    icondx = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.nameserve
