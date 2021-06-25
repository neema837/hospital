from django.db import models

# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='dept', blank=True)

    class Mete:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse("product_by_dept", args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Doctor(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='image', blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Mete:
        ordering = ('name',)
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

    def __str__(self):
        return '{}'.format(self.name)


class Booking(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField()
    num = models.IntegerField()
    address = models.TextField()
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
