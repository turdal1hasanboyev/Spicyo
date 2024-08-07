from django.db import models

from apps.common.models import BaseModel


class Recipe(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
