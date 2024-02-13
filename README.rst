Django Admin Updates
=============================

|image1| |image2| |image3| |image4|

A reusable Django application that adds simple admin-panel updates
to any model, allowing Django Administrators to communicate
on certain objects more easily.

|image5|

Quickstart
----------

-  Install Django Admin Updates:

   ::

      copy the admin_updates folder to your project root

-  Add it to your ``INSTALLED_APPS``:

   .. code:: python

       INSTALLED_APPS = (
           ...
           'admin_updates',
           ...
       )

- Run database migrations

   .. code:: bash

       $ manage.py migrate

- Now, simply add the ``UpdateInline`` to any ``ModelAdmin``

   .. code:: python

       from admin_updates.admin import UpdateInline

       class MyModelAdmin(admin.ModelAdmin):
           model = MyModel
           inlines = [UpdateInline,]

Settings
--------

-  ``admin_updates_SHOW_EMPTY``: Should the comment forms display an empty
   form field by default? (Default: ``False``)

   Example:

   .. code:: python

       admin_updates_SHOW_EMPTY = True

-  ``admin_updates_FORM_CLASS``: Override the default class used for the comment
   form. (Default: ``"admin_updates.forms.UpdateInlineForm"``)

   Example:

   .. code:: python

       admin_updates_FORM_CLASS = "myapp.forms.MyCustomUpdateForm"

-  ``admin_updates_FORMSET_CLASS``: Override the default class used for the comment
   formset. (Default: ``"admin_updates.forms.UpdateInlineFormset"``)

   Example:

   .. code:: python

       admin_updates_FORMSET_CLASS = "myapp.forms.MyCustomUpdateFormSet"

Features
--------

-  Generic comment model to add updates to any object
-  Simple configuration without the overhead of the Django Comments Framework
-  Overridable Form and Formset classes

Support
-------

**Python**

-  2.7
-  3.4
-  3.5
-  3.6

**Django**

-  1.8
-  1.9
-  1.10
-  1.11
-  2.0

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_dev.txt
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ tox

Credits
-------

Original inspiration from Dryice Liu's answer on the following post:

https://stackoverflow.com/a/30338979/3768332

Tools used in rendering this package:

-  `Cookiecutter`_
-  `cookiecutter-djangopackage`_

.. _django-mailer: https://github.com/pinax/django-mailer
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage

.. |image1| image:: https://img.shields.io/pypi/v/django-admin-comments.svg
   :target: https://pypi.python.org/pypi/django-admin-comments
.. |image2| image:: https://img.shields.io/travis/jamiecounsell/django-admin-comments.svg
   :target: https://travis-ci.org/jamiecounsell/django-admin-comments
.. |image3| image:: https://img.shields.io/codecov/c/github/jamiecounsell/django-admin-comments.svg
   :target: https://codecov.io/gh/jamiecounsell/django-admin-comments
.. |image4| image:: https://img.shields.io/badge/Fork%20on%20Github--brightgreen.svg?colorB=4dbf30
   :target: https://github.com/jamiecounsell/django-admin-comments/
.. |image5| image:: https://user-images.githubusercontent.com/2321599/34967909-e8eb0032-fa33-11e7-81c2-460c7104a82a.png
