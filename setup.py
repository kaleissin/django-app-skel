#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

README_FILE = open('README.rst')
try:
    long_description = README_FILE.read()
finally:
    README_FILE.close()

setup(name='django-{{ app_name }}',
        version='0.1',
        packages=['{{ app_name }}'],
        package_dir = {'': 'src',},
        include_package_data=True,
        zip_safe=False,
        platforms=['any'],
        description='SET THIS, make it short and snappy. Max 66 chars',
        author_email='SET.THIS@example.com',
        author='SET THIS',
        long_description=long_description,
        classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Application Frameworks',
                'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
