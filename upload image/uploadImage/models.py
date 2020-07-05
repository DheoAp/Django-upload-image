from django.db import models
from django.urls import reverse

# Create your models here.

class Upload(models.Model):
    nama    = models.CharField(max_length=50)
    Image   = models.ImageField(upload_to='images/', blank=True)
    Image2   = models.ImageField(upload_to='images/', blank=True)
    Image3   = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return '{}.{}'.format(self.id,self.nama)

    def get_absolute_url(self):
        return reverse('succes') 


# Di sini upload_to akan ditentukan, ke direktori mana gambar harus berada,
# secara default Django membuat direktori di bawah direktori media yang 
# akan secara otomatis dibuat ketika kita mengunggah gambar.