==========================
API Example based on Flask
==========================

This repository is used as example Flask project in `API based on Flask`_ post.
It borrows entities from `Abstract Internal Messaging System`_ as
API resources.

Install requirements and run gunicorn.

.. code-block:: console

    $ pip install -r requirements.txt
    $ gunicorn messaging_api:app

.. _API based on Flask: http://marselester.ru/api-based-on-flask.html
.. _Abstract Internal Messaging System: https://github.com/marselester/abstract-internal-messaging
