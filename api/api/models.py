from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100, blank=True)
def __str__(self):
    return '%s' % (self.name)

category = Category(
    name="Computer and Accessories",
    desc="abc desc"
)
category.save()