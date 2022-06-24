from django.db import models

# Create your models here.
class aboutcontent(models.Model):
    title = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='aboutcontent/', blank=False)
    def __str__(self):
        return self.title
