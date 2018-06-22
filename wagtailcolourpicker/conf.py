from django.conf import settings


SETTINGS_PREFIX = 'WAGTAILCOLOURPICKER'
SETTINGS_DEFAULTS = {
    'ICON': [
        'm512 152.363c156.075 231.979 256 393.515 256 533.461 0 139.435-114.816 '
        '252.843-256 252.843s-256-113.408-256-252.8c0-139.989 99.925-301.525 '
        '256-533.504zm0-152.363c-207.787 307.072-341.333 499.157-341.333 685.867 '
        '0 186.795 152.704 338.133 341.333 338.133s341.333-151.339 '
        '341.333-338.133c0-186.709-133.547-378.795-341.333-685.867zm113.323 '
        '512c41.344 148.651-17.323 292.651-113.323 331.989 141.568 20.267 '
        '255.744-147.883 113.323-331.989z'
    ],
    'COLOURS': {
        'black': '#000000',
        'white': '#ffffff'
    }
}


def get_setting(name):
    setting_key = '{}_{}'.format(SETTINGS_PREFIX, name)
    return getattr(settings, setting_key, SETTINGS_DEFAULTS[name])
