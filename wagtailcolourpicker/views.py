from wagtail.admin.modal_workflow import render_modal_workflow

from wagtailcolourpicker.forms import ColourForm
from wagtailcolourpicker.utils.colour import get_feature_name_list, get_feature_name_upper


def chooser(request):
    if request.method == 'POST':
        form = ColourForm(request.POST)

        if form.is_valid():

            feature_name = ''
            if form.cleaned_data.get('colour'):
                feature_name = get_feature_name_upper(form.cleaned_data.get('colour'))

            all_features = get_feature_name_list()

            return render_modal_workflow(
                request, None, None, None,
                json_data={
                    'step': 'colour_chosen',
                    'toggled_feature': feature_name,
                    'all_features': all_features
                }
            )
    else:
        form = ColourForm()

    return render_modal_workflow(
        request, 'colourpicker/chooser/chooser.html', None,
        {'form': form},
        json_data={'step': 'chooser'}
    )
