from django.urls import path

from wagtailcolourpicker.views import chooser


app_name = 'wagtailcolourpicker'

urlpatterns = [
    path('chooser/', chooser, name='chooser'),
]
