Wagtail ColourPicker
====================

A colour picker for Wagtail Draftjs.

Installation
------------

.. code:: bash

   pip install -e git+https://github.com/AccentDesign/wagtailcolourpicker.git#egg=wagtailcolourpicker

Setup
-----

Add to installed app:

.. code:: python

   INSTALLED_APPS = [
      ...
      'wagtailcolourpicker',
      ...
   ]

Settings
--------

.. code:: python

   # picker icon
   WAGTAILCOLOURPICKER_ICON = ['...']
   # Colours
   WAGTAILCOLOURPICKER_COLOURS = (
        ('black', '#000000'),
        ('white', '#ffffff'),
        ('aqua', '#7fdbff'),
        ('blue', '#0074d9'),
        ('navy', '#001f3f'),
        ('teal', '#39cccc'),
        ('green', '#2ecc40'),
        ('olive', '#3d9970'),
        ('lime', '#01ff70'),
    )

Documentation
-------------

TODO

Screenshots
-----------

.. figure:: screen_1.png
   :width: 728 px

Picker

.. figure:: screen_2.png
   :width: 728 px

Selected Text

Example site with docker
------------------------

Clone the repo

.. code:: bash

    $ git clone https://github.com/AccentDesign/wagtailcolourpicker.git

Run the docker container

.. code:: bash

    $ cd wagtailcolourpicker
    $ docker-compose up

Create yourself a superuser

.. code:: bash

    $ docker-compose exec app bash
    $ python manage.py createsuperuser

Go to http://127.0.0.1:8000/cms and add a new basic page

Testing
-------

TODO