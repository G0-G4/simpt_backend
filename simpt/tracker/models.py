from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

# Create your models here.


class Section(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#ffffff', validators=[
        RegexValidator(regex=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Status(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, null=True, blank=True)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.SmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], blank=True, null=True)
    start_datetime = models.DateTimeField()
    due_datetime = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
