import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

from wagtailcolourpicker.conf import get_setting


def get_feature_name(name):
    feature = 'colour_%s' % name
    return feature


def get_feature_name_upper(name):
    return get_feature_name(name).upper()


def get_feature_list():
    return [get_feature_name_upper(c[0]) for c in get_setting('COLOURS')]


def register_color_feature(name, color, features):
    feature_name = get_feature_name(name)
    type_ = get_feature_name_upper(name)
    tag = 'span'
    detection = f'{tag}[style="color: {color};"]'

    control = {
        'type': type_,
        'icon': get_setting('ICON'),
        'description': color,
        'style': {'color': color}
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {detection: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'style': {
                            'color': color
                        }
                    }
                }
            }
        },
    })

    features.default_features.append(feature_name)


def register_all_colour_features(features):
    for c in get_setting('COLOURS'):
        register_color_feature(c[0], c[1], features)
