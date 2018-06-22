from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtailcolourpicker.conf import get_setting


class ColourRadioSelect(forms.widgets.RadioSelect):
    option_template_name = 'colourpicker/forms/widgets/colour_option.html'


class ColourForm(forms.Form):
    colour = forms.ChoiceField(
        label=_("Colours"),
        choices=get_setting('COLOURS'),
        widget=ColourRadioSelect,
        required=False
    )
