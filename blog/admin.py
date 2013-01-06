from django.contrib import admin
from django import forms
from models import Entry
from django.db import models
from redactor_test.redactor.widgets import RedactorWidget

class EntryAdmin(admin.ModelAdmin):
    #body = forms.CharField(widget=RedactorWidget())
    formfield_overrides = {
        models.TextField: {'widget': RedactorWidget},
    }

admin.site.register(Entry, EntryAdmin)
