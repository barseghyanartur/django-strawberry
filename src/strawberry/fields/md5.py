import logging

from django.db.models import CharField
from six import string_types
from .helpers import generate_md5_hash, get_prepopulated_value

__title__ = 'strawberry.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MD5Field',
)

LOGGER = logging.getLogger(__name__)


class MD5Field(CharField):
    """MD5 field."""

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 50)

        # Auto-populated md5 hash is not editable unless told so
        self.populate_from = kwargs.pop('populate_from', None)
        if self.populate_from:
            kwargs.setdefault('editable', False)

        # Unique_with value can be string or tuple
        self.unique_with = kwargs.pop('unique_with', ())
        if isinstance(self.unique_with, string_types):
            self.unique_with = (self.unique_with,)

        if self.unique_with:
            # We will do "manual" granular check below
            kwargs['unique'] = False

        # Set db_index=True unless it's been set manually.
        if 'db_index' not in kwargs:
            kwargs['db_index'] = True

        # When using model inheritance, set manager to search for matching
        # md5 hash values.
        self.manager = kwargs.pop('manager', None)
        self.manager_name = kwargs.pop('manager_name', None)

        self.always_update = kwargs.pop('always_update', True)

        super(MD5Field, self).__init__(*args, **kwargs)

    def deconstruct(self):
        """Deconstruct.

        Returns:
            `tuple`
        """
        name, path, args, kwargs = super(MD5Field, self).deconstruct()

        if self.max_length == 50:
            kwargs.pop('max_length', None)

        if self.populate_from is not None:
            kwargs['populate_from'] = self.populate_from
            if self.editable is not False:
                kwargs['editable'] = self.editable

        if self.unique_with != ():
            kwargs['unique_with'] = self.unique_with
            kwargs.pop('unique', None)

        kwargs.pop('db_index', None)

        if self.manager is not None:
            kwargs['manager'] = self.manager

        if self.manager_name is not None:
            kwargs['manager_name'] = self.manager_name

        if self.always_update:
            kwargs['always_update'] = self.always_update

        if 'manager' in kwargs:
            del kwargs['manager']

        return name, path, args, kwargs

    def pre_save(self, instance, add):
        """Pre-save.

        Args:
            instance:
            add:

        Returns:
            `str`
        """
        # Get currently entered md5 hash value
        value = self.value_from_object(instance)

        if self.manager is not None:
            manager = self.manager
        elif self.manager_name is not None:
            manager = getattr(self.model, self.manager_name)
        else:
            manager = None

        # Auto-populate
        if self.always_update or (self.populate_from and not value):
            value = get_prepopulated_value(self, instance)

            # pragma: nocover
            if __debug__ and not value and not self.blank:
                LOGGER.debug(
                    'Failed to populate md5 hash {}.{} from {}'.format(
                        instance._meta.object_name,
                        self.name,
                        self.populate_from
                    )
                )

        if value:
            hash_value = generate_md5_hash(value)
        else:
            hash_value = None

            if not self.blank:
                hash_value = instance._meta.model_name
            elif not self.null:
                hash_value = ''

            # Ensure the hash_value is unique (if required)
            # if self.unique or self.unique_with:
            #     # TODO

            assert hash_value, 'value is filled before saving'

        # Make the updated md5 hash available as instance attribute
        setattr(instance, self.name, hash_value)

        return hash_value
