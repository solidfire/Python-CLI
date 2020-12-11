from __future__ import print_function
import sys
from codecs import open
import os
import json

from setuptools import setup, find_packages

DESCRIPTION = "A python client and CLI for accessing the SolidFire API."

if os.path.exists('README.rst'):
    with open('README.rst', 'r', 'utf-8') as readme_file:
        LONG_DESCRIPTION = readme_file.read()
else:
    LONG_DESCRIPTION = DESCRIPTION

clisdkversion = ''
with open('cli_version.json') as versionfile:
    versioninfo = json.load(versionfile)
    clisdkversion = versioninfo['version']

setup(
    name='solidfire-cli',
    version=clisdkversion,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=["element.tests"]),
    license='Apache License 2.0',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'sfcli=element.cli.cli:cli',
        ],
    },
    install_requires=[
        'click >= 5',
		'future',
		'setuptools',
        'simplejson',
        'jsonpickle >= 0.9.3',
		'solidfire-sdk-python >= 1.2',
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 2.7',
    ],
)
