from django.db import models

class Floor(models.Model):
    floorNumber = models.IntegerField(default=0)
    availableWashrooms = models.IntegerField(default=0)
    totalWashrooms = models.IntegerField(default=0)
    #contains a map
    #should contain an array of washrooms on this floor

class Washroom(models.Model):
    availableStalls = models.IntegerField(default=0)
    totalStalls = models.IntegerField(default=0)
    gender = models.CharField(default='f', max_length=1)
    #should contain an array of stalls in this washroom

class Stall(models.Model):
    isAvailable = models.BooleanField(default=False)
