from django.db import models

from six import python_2_unicode_compatible

from strawberry.fields import MD5Field

__all__ = ('Book',)


def strip_synopsis(instance):
    return instance.synopsis.strip()


@python_2_unicode_compatible
class Book(models.Model):
    """Book."""

    # Non-hash fields
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.PositiveIntegerField(default=200)
    stock_count = models.PositiveIntegerField(default=30)

    # Hash fields
    description = models.TextField(null=True, blank=True)
    description_hash = MD5Field(
        populate_from='description',
        null=True,
        blank=True
    )

    summary = models.TextField(null=True, blank=True)
    summary_hash = MD5Field(
        populate_from='summary',
        null=True,
        blank=True,
        strip_whitespace=True
    )

    credits = models.TextField(null=True, blank=True)
    credits_hash = MD5Field(
        populate_from='credits',
        strip_whitespace=False
    )

    synopsis = models.TextField(null=True, blank=True)
    synopsis_hash = MD5Field(
        populate_from=strip_synopsis,
        strip_whitespace=False
    )

    class Meta(object):
        """Meta options."""

        ordering = ["isbn"]

    def __str__(self):
        return self.title
