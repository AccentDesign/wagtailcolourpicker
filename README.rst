Wagtail ColourPicker
====================

A colour picker for Wagtail Draftjs.

Documentation
-------------

TODO

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