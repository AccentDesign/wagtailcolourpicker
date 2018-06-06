from django import forms

from wagtail.core import blocks


class RichTextBlock(blocks.RichTextBlock):

    @property  # changed from cached_property to property for preview to still work
    def field(self):
        from wagtail.admin.rich_text import get_rich_text_editor_widget
        return forms.CharField(
            widget=get_rich_text_editor_widget(self.editor, features=self.features),
            **self.field_options
        )
