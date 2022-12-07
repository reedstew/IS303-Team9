from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_missing = models.CharField(max_length=45)
    age_at_missing = models.IntegerField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "people"


class List(models.Model):
    people = models.ManyToManyField("Person",blank=True)
