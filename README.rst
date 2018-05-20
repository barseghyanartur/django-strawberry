=================
django-strawberry
=================
Additional fields for(ever) Django.

Prerequisites
=============

- Django 1.8, 1.9, 1.10, 1.11 and 2.0.
- Python 2.7, 3.6

Documentation
=============

Documentation is available on `Read the Docs
<http://django-strawberry.readthedocs.io/>`_.

Main features and highlights
============================

- MD5Field.

Installation
============

(1) Install latest stable version from PyPI:

    .. code-block:: sh

        pip install django-strawberry

    or latest stable version from GitHub:

    .. code-block:: sh

        pip install https://github.com/barseghyanartur/django-strawberry/archive/stable.tar.gz

    or latest stable version from BitBucket:

    .. code-block:: sh

        pip install https://bitbucket.org/barseghyanartur/django-strawberry/get/stable.tar.gz

Usage
=====

MD5 field
---------
In case you want to have an MD5 field populated from another field of the same
model.

**myapp/models.py**

.. code-block:: python

    from django.db import models
    from strawberry.fields import MD5Field

    class MyModel(models.Model):

        title = models.CharField(max_length=255)
        title_hash = MD5Field(populate_from='title')

        def __str__(self):
            return self.title

**myapp/example.py**

.. code-block:: python

    from myapp.models import MyModel

    mymodel = MyModel.objects.create(title="Lorem7")
    print(mymodel.title_hash)
    'd48a712e77902d0558a3721d9a4740c9'

Testing
=======

Project is covered with tests.

To test with all supported Python/Django versions type:

.. code-block:: sh

    tox

To test against specific environment, type:

.. code-block:: sh

    tox -e py36-django110

To test just your working environment type:

.. code-block:: sh

    ./runtests.py

To run a single test in your working environment type:

.. code-block:: sh

    ./runtests.py src/strawberry/tests/test_fields.py

Or:

.. code-block:: sh

    ./manage.py test strawberry.tests.test_fields

It's assumed that you have all the requirements installed. If not, first
install the test requirements:

.. code-block:: sh

    pip install -r examples/requirements/test.txt

Writing documentation
=====================

Keep the following hierarchy.

.. code-block:: text

    =====
    title
    =====

    header
    ======

    sub-header
    ----------

    sub-sub-header
    ~~~~~~~~~~~~~~

    sub-sub-sub-header
    ^^^^^^^^^^^^^^^^^^

    sub-sub-sub-sub-header
    ++++++++++++++++++++++

    sub-sub-sub-sub-sub-header
    **************************

License
=======

GPL 2.0/LGPL 2.1

Support
=======

For any issues contact me at the e-mail given in the `Author`_ section.

Author
======

Artur Barseghyan <artur.barseghyan@gmail.com>
