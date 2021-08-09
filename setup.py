#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['prompt-toolkit>=3.0.19', 'jsonschema>=3.2.0']

test_requirements = [ ]

setup(
    author="Ross Blair",
    author_email='rosswilsonblair@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CLI tool to build bids-stats-models.",
    entry_points={
        'console_scripts': [
            'bids_stats_model_builder=bids_stats_model_builder.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bids_stats_model_builder',
    name='bids_stats_model_builder',
    packages=find_packages(include=['bids_stats_model_builder', 'bids_stats_model_builder.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rwblair/bids_stats_model_builder',
    version='0.1.0',
    zip_safe=False,
)