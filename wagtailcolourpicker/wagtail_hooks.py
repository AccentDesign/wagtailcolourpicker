from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse, path, include
from django.utils.html import format_html_join, format_html
from django.utils.translation import ugettext as _

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.core import hooks

from wagtailcolourpicker.conf import get_setting
from wagtailcolourpicker.utils.colour import register_all_colour_features


@hooks.register('register_admin_urls')
def register_admin_urls():
    from wagtailcolourpicker import urls
    return [
        path('wagtailcolourpicker/', include((urls, 'wagtailcolourpicker'))),
    ]


@hooks.register('insert_editor_css')
def editor_css():
    css_files = [
        'colourpicker/css/colourpicker.css',
    ]
    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}">',
        ((static(filename), ) for filename in css_files)
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
        '<script src="{0}"></script>',
        ((static(filename), ) for filename in js_files)
    )
    js_includes += format_html(
        "<script>window.chooserUrls.colourChooser = '{0}';</script>",
        reverse('wagtailcolourpicker:chooser')
    )
    return js_includes


@hooks.register('register_rich_text_features')
def register_textcolour_feature(features):
    # register all colour features
    register_all_colour_features(features)

    # register the color picker
    feature_name = 'textcolour'
    type_ = feature_name.upper()

    control = {
        'type': type_,
        'icon': get_setting('ICON'),
        'description': _('Text Colour'),
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(control)
    )

    features.default_features.append(feature_name)
