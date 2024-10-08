from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SubEmail(BaseModel):
    sub_email = models.EmailField(max_length=225, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.sub_email}"
