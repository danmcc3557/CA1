import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse


class Advert(models.Model):
    title = models.CharField(max_length=255)
    #image = models.ImageField(blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advert_detail', args=[str(self.id)])

"""
import uuid
from django.db import models
from django.urls import reverse


class Advert(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='advert', blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True,blank=True,null=True)
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'advert'
        verbose_name_plural = 'advert'

    def get_absolute_url(self):
        return reverse('advert:advert_detail', args=[str(self.id)])

    def __str__(self):
        return self.name"""