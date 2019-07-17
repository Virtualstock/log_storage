#!/usr/bin/env python

import os
from setuptools import setup

long_description = 'Please see our GitHub README'
if os.path.exists('README.md'):
    long_description = open('README.md').read()

setup(
    name='log_storage',
    version='0.7.0',
    license='MIT',
    description='Log handler to store messages with a database record and optional file storage.',
    keywords=['Django', 'Log', 'App'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Virtualstock',
    author_email='development.team@virtualstock.com',
    url='https://github.com/virtualstock/log_storage/',
    packages=['log_storage', 'log_storage.migrations'],
    include_package_data=True,
    install_requires=['django'],
)
