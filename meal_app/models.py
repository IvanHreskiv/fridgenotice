from django.db import models
from django.urls import reverse
from django.utils import timezone


class Meal(models.Model):
    name = models.CharField(max_length=30, unique=True)
    detail = models.CharField(max_length=150, blank=True)
    date_field = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("meals:detail", kwargs={"name": self.name})
