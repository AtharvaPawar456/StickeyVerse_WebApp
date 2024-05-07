# stickeyverse_app/models.py

from django.db import models


class Sticker(models.Model):
    id = models.AutoField(primary_key=True)
    stickername = models.CharField(max_length=150)
    image = models.ImageField(upload_to='stickeyverse_app/stickers/')
    category = models.CharField(max_length=150, default="")
    material = models.CharField(max_length=150, default="")
    price = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    description = models.TextField()
    
    def __str__(self):
        return self.stickername
    
