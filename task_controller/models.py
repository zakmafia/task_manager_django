from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField('Name', max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    images = models.ImageField('Image', upload_to='photos/orders')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField('Name', max_length=150, unique=True)
    time_counter = models.TimeField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.name