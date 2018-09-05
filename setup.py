#!/usr/bin/env python

from setuptools import setup

setup(
    name='log_storage',
    version='0.4.0',
    description='Log handler to store messages with a database record and optional file storage.',
    author='Virtualstock',
    author_email='development.team@virtualstock.com',
    url='https://github.com/virtualstock/log_storage/',
    packages=['log_storage', 'log_storage.migrations'],
    include_package_data=True,
    install_requires=['django'],
)
