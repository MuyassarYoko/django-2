from django.db import models as m


# Create your models here.
class Item(m.Model):
    name = m.CharField("Name", max_length=100, unique=True)
    price = m.IntegerField("Price")
    count = m.IntegerField("Count")
    created_at = m.DateTimeField("Created at", auto_now=True)

    def __str__(self):
        return self.name
