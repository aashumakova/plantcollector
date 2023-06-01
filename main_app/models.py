from django.db import models
from django.urls import reverse
from datetime import date

WEEKDAYS = (
    ('Sun', 'Sunday'),
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
)

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    light = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
    def watered_for_the_week(self):
        return self.watering_set.filter(date=date.today()).count() >= len(WEEKDAYS)

class Watering(models.Model):
    date = models.DateField('Watering Date')
    weekday = models.CharField(
        max_length=3,
        choices=WEEKDAYS,
        default=WEEKDAYS[0][0]
    )
    #Create a plant_id FK
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_weekday_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
