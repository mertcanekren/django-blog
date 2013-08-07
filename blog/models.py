from django.db import models
from django.core.validators import validate_slug

class makale(models.Model):
    baslik = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    giris = models.TextField(max_length=500)
    makale = models.TextField()
    yayin_tarihi = models.DateTimeField("Yayinlanma Tarihi")
     
    def __unicode__(self):
        return self.slug