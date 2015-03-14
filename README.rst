sentry-rienann
=============

An extension for Sentry to send errors metrics to riemann.

Install
-------

Install the package with ``pip``::

    pip install sentry-riemann


Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and select the
"Riemann" tab. Enter the Riemann host, port and prefix for metrics:


After installing and configuring, make sure to restart sentry-worker for the
changes to take into effect.


This plugin is heavily based on _riemann-statsd: https://github.com/dreadatour/sentry-statsd
