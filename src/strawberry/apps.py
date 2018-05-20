"""
Apps.
"""

from django.apps import AppConfig

__title__ = 'strawberry.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'strawberry'
    label = 'strawberry'
