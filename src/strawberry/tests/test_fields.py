# -*- coding: utf-8 -*-
"""
Test fields.
"""

from __future__ import absolute_import, unicode_literals

import hashlib
import unittest

import pytest

import factories

from .base import BaseTestCase

__title__ = 'strawberry.tests.test_fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'TestFields',
)


BOOK_DATA = {
    'title': "CHAPTER II. The Pool of Tears.",
    'summary': "Alice spots another creature in the pool, swimming far "
               "off. She sees that it is a mouse, who has also slipped "
               "into the pool of tears. Alice thinks she might as well "
               "try speaking to the mouse but he doesn't seem to "
               "understand English, so she tries addressing him in "
               "French. The first phrase she thinks of is “Ou est ma "
               "chatte?“ which means “Where is my cat?“ The mouse is "
               "suitably unnerved. Alice protests that the mouse would "
               "like her cat, Dinah, and proceeds to list her virtues. "
               "The mouse is very offended.",
    'description': "As she said these words her foot slipped, and in "
                   "another moment, splash! she was up to her chin in "
                   "salt water. Her first idea was that she had somehow "
                   "fallen into the sea, ‘and in that case I can go back "
                   "by railway,’ she said to herself. (Alice had been to "
                   "the seaside once in her life, and had come to the "
                   "general conclusion, that wherever you go to on the "
                   "English coast you find a number of bathing machines "
                   "in the sea, some children digging in the sand with "
                   "wooden spades, then a row of lodging houses, and "
                   "behind them a railway station.) However, she soon "
                   "made out that she was in the pool of tears which she "
                   "had wept when she was nine feet high.",
}


@pytest.mark.django_db
class TestFields(BaseTestCase):
    """Test fields."""

    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpClass(cls):
        cls.book = factories.BookFactory(**BOOK_DATA)

    def test_filter_by_field(self):
        """Filter by field."""
        md5 = hashlib.md5()

        summary_text = BOOK_DATA['summary'].encode('utf8')

        md5.update(summary_text)
        self.assertEqual(
            self.book.summary_hash,
            md5.hexdigest()
        )

        md5 = hashlib.md5()
        description_text = BOOK_DATA['description'].encode('utf8')
        md5.update(description_text)
        self.assertEqual(
            self.book.description_hash,
            md5.hexdigest()
        )


if __name__ == '__main__':
    unittest.main()
