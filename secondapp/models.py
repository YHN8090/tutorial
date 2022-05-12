from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)

class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()

    class Meta:
        db_table = 'army_shop'
        managed= False

