from wagtail.admin.modal_workflow import render_modal_workflow

from wagtailcolourpicker.forms import ColourForm
from wagtailcolourpicker.models import Colour


def chooser(request):
    if request.method == 'POST':
        form = ColourForm(request.POST)

        if form.is_valid():

            colour = None
            created = False

            if form.cleaned_data.get('new'):
                code = form.cleaned_data['new'].upper()
                colour, created = Colour.objects.get_or_create(code=code)

            elif form.cleaned_data.get('colour'):
                colour = form.cleaned_data['colour']

            return render_modal_workflow(
                request, None, 'colourpicker/chooser/chosen.js',
                {
                    'colour': colour,
                    'created': created,
                    'colours': [c.feature_name_upper for c in Colour.objects.all()]
                }
            )
    else:
        form = ColourForm()

    return render_modal_workflow(
        request, 'colourpicker/chooser/chooser.html', 'colourpicker/chooser/chooser.js',
        {'form': form}
    )
