==========================
API Example based on Flask
==========================

This repository is used as example Flask project in `API based on Flask`_ post.

Consider Flask application from **messaging** package as deployed on
``https://app.example.com``. You can sign in there as user *marsel*
(password is *123*). WSGI application from **messaging_api** module
should be assumed as deployed on ``https://api.example.com``.

Install requirements and run gunicorn.

.. code-block:: console

    $ pip install -r requirements.txt
    $ gunicorn -b 127.0.0.1:5000 messaging:app
    $ gunicorn -b 127.0.0.1:8000 messaging_api:app

Sign in on ``http://127.0.0.1:5000`` and now you can try to make
authenticated requests to API ``http://127.0.0.1:8000/v3/messages/``.

.. _API based on Flask: http://marselester.ru/api-based-on-flask.html
