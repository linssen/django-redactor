from django.db import models
from django import forms

class Entry(models.Model):
    body = models.TextField()
