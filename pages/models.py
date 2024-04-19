from django.db import models

# Create your models here.
class Chef(models.Model):
    full_name = models.CharField(max_length=100)

    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    locale = models.CharField(max_length=100, default="none")
    icon = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.full_name


