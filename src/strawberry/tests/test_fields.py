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
    'TestMD5Field',
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
    'credits': """
               Charles Lutwidge Dodgson under the pseudonym Lewis Carroll.
               """,
    'synopsis': """
                Chapter Two – The Pool of Tears: Chapter Two opens with Alice   
                growing to such a tremendous size her head hits the ceiling.   
                Alice is unhappy and, as she cries, her tears flood the   
                hallway. After shrinking down again due to a fan she had picked    
                up, Alice swims through her own tears and meets a Mouse, who is    
                swimming as well. She tries to make small talk with him in    
                elementary French (thinking he may be a French mouse) but her    
                opening gambit "Où est ma chatte?" ("Where is my cat?") offends 
                the mouse and he tries to escape her.
                """,
}

BOOK_DATA_UPDATE = {
    'title': "CHAPTER II. Summary and description.",
    'summary': "‘What a curious feeling!’ said Alice; ‘I must be shutting "
               "up like a telescope.’ However, she soon made out that she "
               "was in the pool of tears which she had wept when she was "
               "nine feet high.",
    'description': "So she was considering in her own mind (as well as "
                   "she could, for the hot day made her feel very sleepy "
                   "and stupid), whether the pleasure of making a "
                   "daisy-chain would be worth the trouble of getting up "
                   "and picking the daisies, when suddenly a White Rabbit "
                   "with pink eyes ran close by her. However, she soon "
                   "made out that she was in the pool of tears which she "
                   "had wept when she was nine feet high.",
    'credits': """
               Lewis Carroll (real name Charles Lutwidge Dodgson).
               """,
    'synopsis': """
                Chapter One – Down the Rabbit Hole: Alice, a girl of seven 
                years, is feeling bored and drowsy while sitting on the 
                riverbank with her elder sister. She then notices a talking, 
                clothed White Rabbit with a pocket watch run past. She follows 
                it down a rabbit hole when suddenly she falls a long way to a 
                curious hall with many locked doors of all sizes. She finds a 
                small key to a door too small for her to fit through, but 
                through it she sees an attractive garden. She then discovers 
                a bottle on a table labelled "DRINK ME," the contents of which 
                cause her to shrink too small to reach the key which she has 
                left on the table. She eats a cake with "EAT ME" written on 
                it in currants as the chapter closes.
                """

}


@pytest.mark.django_db
class TestMD5Field(BaseTestCase):
    """Test MD5 field.

    - description_hash is nullable, auto-updated field, with auto whitespace
      strip.
    - summary_hash is nullable, auto-updated field, with auto whitespace
      strip.
    - credits_hash is non-nullable, auto-updated field.
    - synopsis_hash is non-nullable, auto-updated field, with manual
      whitespace strip.
    """

    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.book = factories.BookFactory(**BOOK_DATA)

    def _test_filter_by_field(self, model_hash_field, non_hashed_value):
        """Test filter by field.

        Args:
            model_hash_field:
            non_hashed_value:

        Returns:

        """
        md5 = hashlib.md5()
        text = non_hashed_value.encode('utf8')
        md5.update(text)
        self.assertEqual(
            model_hash_field,
            md5.hexdigest()
        )

    def test_filter_by_field(self):
        """Filter by field."""
        self._test_filter_by_field(
            self.book.summary_hash,
            BOOK_DATA['summary']
        )

        self._test_filter_by_field(
            self.book.description_hash,
            BOOK_DATA['description']
        )

        self._test_filter_by_field(
            self.book.credits_hash,
            BOOK_DATA['credits']
        )

        self._test_filter_by_field(
            self.book.synopsis_hash,
            BOOK_DATA['synopsis'].strip()
        )

    def test_filter_by_field_check_update(self):
        """Filter by field, check value update."""
        self.book.summary = BOOK_DATA_UPDATE['summary']
        self.book.description = BOOK_DATA_UPDATE['description']
        self.book.credits = BOOK_DATA_UPDATE['credits']
        self.book.synopsis = BOOK_DATA_UPDATE['synopsis']
        self.book.save()

        self._test_filter_by_field(
            self.book.summary_hash,
            BOOK_DATA_UPDATE['summary']
        )

        self._test_filter_by_field(
            self.book.description_hash,
            BOOK_DATA_UPDATE['description']
        )

        self._test_filter_by_field(
            self.book.credits_hash,
            BOOK_DATA_UPDATE['credits']
        )

        self._test_filter_by_field(
            self.book.synopsis_hash,
            BOOK_DATA_UPDATE['synopsis'].strip()
        )


if __name__ == '__main__':
    unittest.main()
