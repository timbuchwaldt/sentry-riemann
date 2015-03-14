#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.3.3',
    'riemann-client',
]

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='sentry-riemann',
    version='0.0.2',
    author='Tim Buchwaldt',
    author_email='tim@buchwaldt.ws',
    url='http://github.com/timbuchwaldt/sentry-riemann',
    description='A Sentry extension which send errors stats to Riemann',
    long_description=readme,
    license='WTFPL',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'sentry_riemann = sentry_riemann.plugin:RiemannPlugin'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development'
    ],
    keywords='sentry riemann',
)
