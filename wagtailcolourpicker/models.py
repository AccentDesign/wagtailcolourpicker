from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.core.rich_text import features as feature_registry


class Colour(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ['code', ]

    def __str__(self):
        return self.code.upper()

    @property
    def feature_name(self):
        return f'colour_{self}'

    @property
    def feature_name_upper(self):
        return self.feature_name.upper()

    def register_inline_style(self, features):
        colour = str(self)
        type_ = self.feature_name.upper()
        tag = 'span'
        detection = f'{tag}[style="color: {colour};"]'

        control = {
            'type': type_,
            'label': 'C',
            'description': colour,
            'style': {'color': colour}
        }

        features.register_editor_plugin(
            'draftail', self.feature_name, draftail_features.InlineStyleFeature(control)
        )

        features.register_converter_rule('contentstate', self.feature_name, {
            'from_database_format': {
                detection: InlineStyleElementHandler(type_)
            },
            'to_database_format': {
                'style_map': {
                    type_: {
                        'element': tag,
                        'props': {
                            'style': {
                                'color': colour
                            }
                        }
                    }
                }
            },
        })

        features.default_features.append(self.feature_name)


@receiver(post_save, sender=Colour)
def add_colour(instance, **kwargs):
    def func():
        instance.register_inline_style(feature_registry)
    transaction.on_commit(func)
