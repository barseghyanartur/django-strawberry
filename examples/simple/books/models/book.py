from django.db import models

from six import python_2_unicode_compatible

from strawberry.fields import MD5Field

__all__ = ('Book',)


@python_2_unicode_compatible
class Book(models.Model):
    """Book."""

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    description_hash = MD5Field(populate_from='description')
    summary = models.TextField(null=True, blank=True)
    summary_hash = MD5Field(populate_from='summary')
    publication_date = models.DateField()
    isbn = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.PositiveIntegerField(default=200)
    stock_count = models.PositiveIntegerField(default=30)

    class Meta(object):
        """Meta options."""

        ordering = ["isbn"]

    def __str__(self):
        return self.title
