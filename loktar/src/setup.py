#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages
from pip.req import parse_requirements


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [str(i.req) for i in parse_requirements("requirements.txt", session=False)]
test_requirements = [str(i.req) for i in parse_requirements("test_requirements.txt", session=False)]

VERSION = '1002'

setup(
    name='loktar',
    version=str(VERSION),
    description='ci',
    long_description=readme,
    author='Damien Goldenberg',
    author_email='damdam.gold@gmail.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='ci',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
