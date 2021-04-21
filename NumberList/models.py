from django.db import models
from django.conf import settings


# Create your models here.
class Numbers(models.Model):
    Nid = models.IntegerField(primary_key=True)
    numbers = models.IntegerField()
    

    class Meta:
        db_table = 'Numbers'
        managed = True

class Words(models.Model):
    Wid = models.IntegerField(primary_key=True)
    words = models.CharField(max_length=100)
    Nid = models.IntegerField()

    class Meta:
        db_table = "Words"
        managed = True
