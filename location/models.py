from django.db import models

class Party(models.Model):
    title = models.CharField(max_length=50)
    gu = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=1000)
    day = models.CharField(max_length=100)
    des = models.CharField(max_length=2000)
    mid = models.CharField(max_length=100)
    img = models.CharField(max_length=100)

    class Meta:
        db_table = 'festival'
        managed = True