from django import forms
from django.contrib.admin.templatetags.admin_static import static
from django.utils.safestring import mark_safe

class RedactorWidget(forms.Textarea):
    """
    Widget for Redactor
    """
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['class'] = 'redactor'
        super(RedactorWidget, self).__init__(attrs=attrs)

    class Media:
        css = {"screen": ("django-redactor/redactor/redactor.css",)}
        js = ("django-redactor/redactor/redactor.js", "django-redactor/js/setup.js",)
