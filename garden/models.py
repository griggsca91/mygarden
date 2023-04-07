import datetime

from django.db import models

class PlantType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    days_to_first_harvest = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
class Plant(models.Model):
    type = models.ForeignKey(PlantType, on_delete=models.CASCADE)
    date_planted = models.DateTimeField("date it was planted")
    garden = models.ForeignKey("Garden", on_delete=models.CASCADE)

    def __str__(self):
        return self.type.name

    def harvest_date(self):
        return self.date_planted + datetime.timedelta(days=self.type.days_to_first_harvest)


class Garden(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField(
            default=None, 
            blank=True, 
            null=True
            )
    lighting_choices = [
            ("FULL_SUN", "Full Sun"),
            ("PARTIAL_SUN", "Partial Sun"),
            ("PARTIAL_SHADE", "Partial Shade"),
            ("FULL_SHADE", "Full Shade"),
            ]
    lighting = models.CharField(
            default="SUNNY",
            choices=lighting_choices,
            max_length=100,
            )

    def __str__(self):
        return self.name
