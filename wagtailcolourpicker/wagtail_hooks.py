from django.db.utils import ProgrammingError
from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html_join, format_html

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.core import hooks

from wagtailcolourpicker.conf import get_setting
from wagtailcolourpicker.models import Colour


@hooks.register('insert_editor_css')
def editor_css():
    css_files = [
        'colourpicker/css/colourpicker.css',
    ]
    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}{1}">',
        ((settings.STATIC_URL, filename) for filename in css_files)
    )
    return css_includes


@hooks.register('insert_editor_js')
def insert_editor_js():
    js_files = [
        # We require this file here to make sure it is loaded before the other.
        'wagtailadmin/js/draftail.js',
        'colourpicker/js/colourpicker.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )
    js_includes += format_html(
        "<script>window.chooserUrls.colourChooser = '{0}';</script>",
        reverse('wagtailcolourpicker:chooser')
    )
    return js_includes


@hooks.register('register_rich_text_features')
def register_textcolour_feature(features):
    # register all colour features
    try:
        for colour in Colour.objects.all():
            colour.register_inline_style(features)
    except ProgrammingError:
        pass

    feature_name = 'textcolour'
    type_ = feature_name.upper()

    control = {
        'type': type_,
        'icon': get_setting('ICON'),
        'description': 'Text Colour',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(control)
    )

    features.default_features.append(feature_name)
