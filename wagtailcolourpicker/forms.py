from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtailcolourpicker.models import Colour


class ColourRadioSelect(forms.widgets.RadioSelect):
    option_template_name = 'colourpicker/forms/widgets/colour_option.html'


class ColourForm(forms.Form):
    colour = forms.ModelChoiceField(
        label=_("Colours"),
        queryset=Colour.objects.all(),
        widget=ColourRadioSelect,
        required=False,
        empty_label=None
    )
    new = forms.CharField(
        label=_("New"),
        required=False
    )
