"""
Base tests.
"""

import logging

from django.test import TransactionTestCase
import pytest

import factories

__title__ = 'strawberry.tests.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseTestCase',
)

LOGGER = logging.getLogger(__name__)


@pytest.mark.django_db
class BaseTestCase(TransactionTestCase):
    """Base test case."""

    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpClass(cls):
        """Set up class."""

        # Create test user.
        cls.user = factories.TestUsernameSuperAdminUserFactory()
