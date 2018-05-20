# -*- coding: utf-8 -*-

import hashlib

__title__ = 'strawberry.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'get_prepopulated_value',
    'generate_md5_hash',
)


def get_prepopulated_value(field, instance):
    """Returns preliminary value based on `populate_from`.

    Args:
        field (:obj:`strawberry.fields.md5.MD5Field`): `MD5Field` instance.
        instance (:obj:`django.db.models.Model`): Django model instance.

    Returns:
        str: Prepopulated value.
    """
    if hasattr(field.populate_from, '__call__'):
        # MD5Field(populate_from=lambda instance: ...)
        return field.populate_from(instance)
    else:
        # MD5Field(populate_from='foo')
        attr = getattr(instance, field.populate_from)
        return callable(attr) and attr() or attr


def generate_md5_hash(value, unique=False):
    """Generate md5 hash.

    Args:
        value (str):
        unique (bool):

    Returns:
        str: Generated MD5 hash.
    """
    md5 = hashlib.md5()
    encoded_value = value.encode('utf8')
    md5.update(encoded_value)
    return md5.hexdigest()
