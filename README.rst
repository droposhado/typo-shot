Typo Shot!
==========

Typo is a script to take screenshot on your website/blog. A simple way to check typography, viewing the page in complete.

Status
---------
- .. image:: https://travis-ci.org/flavertonrr/typo-shot.png
- .. image:: https://img.shields.io/pypi/v/typo-shot.svg
- .. image:: https://img.shields.io/pypi/dm/typo-shot.svg
- .. image:: https://img.shields.io/pypi/dw/typo-shot.svg
- .. image:: https://img.shields.io/pypi/dd/typo-shot.svg
- .. image:: https://img.shields.io/pypi/pyversions/typo-shot.svg

How to use
---------

You just need to provide a ``site.json`` file on your website. In the following format:

::

    {
      "pages": [
        {
          "title": "Title",
          "url": "http://url.com"
        },
        {
          "title": "Title",
          "url": "http://url.com"
        },
        ...
      ]
    }

Command line
---------

::

    typo http://flaverton.com

    typo <url>

Reference
---------

- `Classifiers`_

.. _Classifiers: https://pythonhosted.org/an_example_pypi_project/setuptools.html

License
-------

`License`_

.. _License: LICENSE.txt

