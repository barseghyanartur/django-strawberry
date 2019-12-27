Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.1.2
-----
2019-12-28

- Drop Support for Django versions earlier than 1.11.
- Tested against Python 3.7 and 3.8.
- Tested against Django 2.1, 2.2 and 3.0.
- Upgrade test suite.

0.1.1
-----
2018-05-20

.. note::

    Release supported by `Teamable <https://www.teamable.com/>`_ - an employee
    referral and diversity hiring platform

- Make it possible to auto-strip the whitespace from `populated_from` value.
- More tests.

0.1
---
2018-05-20

.. note::

    Release supported by `Teamable <https://www.teamable.com/>`_ - an employee
    referral and diversity hiring platform

- Initial beta release.
