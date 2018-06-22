from wagtail.admin.modal_workflow import render_modal_workflow

from wagtailcolourpicker.forms import ColourForm
from wagtailcolourpicker.utils.colour import get_feature_list, get_feature_name_upper


def chooser(request):
    if request.method == 'POST':
        form = ColourForm(request.POST)

        if form.is_valid():

            feature = ''
            if form.cleaned_data.get('colour'):
                feature = get_feature_name_upper(form.cleaned_data.get('colour'))

            return render_modal_workflow(
                request, None, 'colourpicker/chooser/chosen.js',
                {
                    'feature': feature,
                    'all_features': get_feature_list()
                }
            )
    else:
        form = ColourForm()

    return render_modal_workflow(
        request, 'colourpicker/chooser/chooser.html', 'colourpicker/chooser/chooser.js',
        {'form': form}
    )
