from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    class Meta:
        ordering = ['day']

    DAYS_OF_THE_WEEK = [
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday')
    ]

    category = models.ForeignKey(
        'Category', null=True, blank=True,
        on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    day = models.CharField(
        max_length=10,
        choices=DAYS_OF_THE_WEEK,
        default='1')
    class_time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        default=datetime.time(10, 0))
    description = models.TextField()
    tagline = models.CharField(
        max_length=250, null=True,
        blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    number_of_sessions = models.IntegerField(
        validators=[MaxValueValidator(50),
                    MinValueValidator(1)], default=10)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
