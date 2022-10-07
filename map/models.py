from django.db import models

class PartyMap(models.Model):
  title = models.CharField(max_length=100)
  lat = models.FloatField()
  lng = models.FloatField()

  class Meta:
    db_table = 'party_map'
    managed = False