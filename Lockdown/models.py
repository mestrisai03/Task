from django.db import models

# Create your models here.


class Country(models.Model):
    cID = models.IntegerField(primary_key=True)
    cName = models.CharField(max_length=100)

    class Meta:
        db_table = 'Country'
        managed = True


class States(models.Model):
    sID = models.IntegerField(primary_key=True)
    sName = models.CharField(max_length=100)
    cID=models.IntegerField()
  
    class Meta:
        db_table = 'State'
        managed = True

class City(models.Model):
    cityID = models.IntegerField(primary_key=True)
    cityName = models.CharField(max_length=100)
    sID=models.IntegerField()
   
    class Meta:
        db_table = 'City'
        managed = True