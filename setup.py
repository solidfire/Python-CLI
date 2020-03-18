from __future__ import print_function
import sys
from codecs import open
import os

from setuptools import setup, find_packages

DESCRIPTION = "A python client and CLI for accessing the SolidFire API."

if os.path.exists('README.rst'):
    with open('README.rst', 'r', 'utf-8') as readme_file:
        LONG_DESCRIPTION = readme_file.read()
else:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name='solidfire-cli',
    version='1.6.0.63',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='SolidFire, Inc.',
    author_email='adam.haid@solidfire.com',
    packages=find_packages(exclude=["element.tests"]),
    license='Apache License 2.0',
    zip_safe=False,
    url='https://github.com/solidfire/solidfire-cli',
    entry_points={
        'console_scripts': [
            'sfcli=element.cli.cli:cli',
        ],
    },
    install_requires=[
        'click >= 6',
        'future',
        'setuptools >= 19.2',
        'simplejson',
        'jsonpickle >= 0.9.3',
        'solidfire-sdk-python >= 1.5',
        'pycryptodome >= 2.6.1',
        'FileLock',
        'getpass2'
    ],
    tests_require=[
        'mock',
        'nose2',
    ],
    keywords=['element'],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 2.7',
    ],
)
