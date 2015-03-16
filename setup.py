# -*- coding: utf-8 -*-
__author__ = 'jayin'

from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    long_description = f.read()

setup(
    name='google.py',
    version='0.1.1',
    description='Search available fast google ip for blocked users',
    long_description=long_description,
    url='https://github.com/Jayin/core.py',
    download_url='https://github.com/Jayin/google.py',
    author='Jayin Ton',
    author_email='tonjayin@gmail.com',
    license='BSD',
    packages=find_packages(),
    include_package_data = True,
    package_data={
    'google': ['data/ips.json'],
},
    entry_points={
        'console_scripts': [
            'google = google.core:main',
        ],
    },
    install_requires=requirements,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Utilities'
    ],
)
