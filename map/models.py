from django.db import models

# Create your models here.
class Block(models.Model):
    geoid = models.CharField(max_length=25, primary_key=True)
    boundary = models.TextField()

class Parcel(models.Model):
    parcelID = models.CharField(max_length=30)
    boundary = models.TextField()
    owner = models.CharField(max_length=200)

class Site(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    parcels = models.ManyToManyField(Parcel)
    boundary = models.TextField()
    sitetype = models.CharField(max_length=50)

    def __str__(self):
        return self.sitetype
