import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse


class Advert(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    #image = models.ImageField(blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advert_detail', args=[str(self.id)])
