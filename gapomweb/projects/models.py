from django.db import models

# Create your models here.
class projectile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    filter = models.TextField(max_length=100, blank=False)
    para = models.TextField(max_length=100, blank=False)
    headn = models.TextField(max_length=100, blank=False)
    image = models.ImageField(upload_to='projectile/', blank=False)
    def __str__(self):
        return self.name
