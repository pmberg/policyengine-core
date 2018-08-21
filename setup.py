#! /usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals, print_function, division, absolute_import
from setuptools import setup, find_packages

general_requirements = [
    'Biryani[datetimeconv] >= 0.10.8',
    'dpath == 1.4.0',
    'enum34 >= 1.1.6',
    'future',
    'numpy >= 1.11, < 1.15',
    'psutil == 5.4.6',
    'PyYAML >= 3.10',
    'sortedcontainers == 1.5.9',
    ]

api_requirements = [
    'flask == 1.0.2',
    'flask-cors == 3.0.2',
    'gunicorn >= 19.7.1',
    ]

dev_requirements = [
    'nose',
    'flake8 >= 3.4.0, < 3.5.0',
    'openfisca-country-template >= 3.2.3, < 4.0.0',
    'openfisca-extension-template >= 1.1.3, < 2.0.0',
    ] + api_requirements

setup(
    name = 'OpenFisca-Core',
    version = '24.0.1',
    author = 'OpenFisca Team',
    author_email = 'contact@openfisca.org',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Information Analysis",
        ],
    description = 'A versatile microsimulation free software',
    keywords = 'benefit microsimulation social tax',
    license = 'https://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url = 'https://github.com/openfisca/openfisca-core',

    data_files = [
        ('share/openfisca/openfisca-core', ['CHANGELOG.md', 'LICENSE.AGPL.txt', 'README.md']),
        ],
    entry_points = {
        'console_scripts': ['openfisca=openfisca_core.scripts.openfisca_command:main', 'openfisca-run-test=openfisca_core.scripts.run_test:main'],
        },
    extras_require = {
        'web-api': api_requirements,
        'dev': dev_requirements,
        'tracker': [
            'openfisca-tracker == 0.4.0',
            ],
        },
    include_package_data = True,  # Will read MANIFEST.in
    install_requires = general_requirements,
    message_extractors = {
        'openfisca_core': [
            ('**.py', 'python', None),
            ],
        },
    packages = find_packages(exclude=['tests*']),
    test_suite = 'nose.collector',
    )
