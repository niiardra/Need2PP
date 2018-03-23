from django.db import models

class Floor(models.Model):
    floorNumber = models.IntegerField()
    #contains a map

class Washroom(models.Model):
    availableStalls = models.IntegerField()
    totalStalls = models.IntegerField()
    gender = models.CharField(max_length=1)
    #should contain an array of stalls

class Stall(models.Model):
    isAvailable = models.BooleanField(default=False)
