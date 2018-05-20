import random

from factory import (
    DjangoModelFactory,
    SubFactory,
    post_generation,
    LazyAttribute,
)

from books.models import Book

from .factory_faker import Faker


__all__ = (
    'BookFactory',
    'BookWithUniqueTitleFactory',
    'SingleBookFactory',
)


class BaseBookFactory(DjangoModelFactory):
    """Base book factory."""

    title = Faker('text', max_nb_chars=100)
    summary = Faker('text')
    description = Faker('text')
    credits = Faker('text')
    synopsis = Faker('text')
    publication_date = Faker('date')
    price = Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    isbn = Faker('isbn13')
    pages = LazyAttribute(
        lambda __x: random.randint(10, 200)
    )

    class Meta(object):
        """Meta class."""

        model = Book
        abstract = True


class BookFactory(BaseBookFactory):
    """Book factory."""


class BookWithUniqueTitleFactory(BaseBookFactory):
    """Book factory with unique title attribute."""

    class Meta(object):
        """Meta class."""

        django_get_or_create = ('title',)


class SingleBookFactory(BaseBookFactory):
    """Book factory, but limited to a single book."""

    id = 999999
    title = "Performance optimisation"

    class Meta(object):
        """Meta class."""

        django_get_or_create = ('id',)
