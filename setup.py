#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name='bcd',
    packages=find_packages(),
    version='@@VERSION@@',
    description='BigClown tool for bigclown developers.',
    author='HARDWARIO s.r.o.',
    author_email='radim.kozak@hardwario.com',
    url='https://github.com/worepix/bcd-tool',
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords=['BigClown', 'bcd', 'developers', 'documentation'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Environment :: Console'
    ],
    entry_points='''
        [console_scripts]
        bcd=bcd.cli:main
    ''',
    long_description=long_description,
    long_description_content_type='text/markdown'
)