from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
