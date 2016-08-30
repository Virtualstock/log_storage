#!/usr/bin/env python

from setuptools import setup

setup(
    name='log_storage',
    version='0.2',
    description='Log handler to store messages with a database record and optional file storage.',
    author='Ronan Klyne',
    author_email='ronan.klyne@virtualstock.co.uk',
    url='http://pypi.v-source.co.uk/',
    packages=['log_storage', 'log_storage.migrations'],
    include_package_data=True,
    install_requires=[]
)
