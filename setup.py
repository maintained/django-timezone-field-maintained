import re
from os import path
from setuptools import setup


# read() and find_version() taken from jezdez's python apps, ex:
# https://github.com/jezdez/django_compressor/blob/develop/setup.py


def read(*parts):
    return open(path.join(path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-timezone-field-maintained',
    version=find_version('timezone_field', '__init__.py'),
    author='Mike Fogel',
    author_email='mike@fogel.ca',
    description=(
        'A Django app providing database and form fields for '
        'pytz timezone objects.'
    ),
    long_description=read('README.rst'),
    url='http://github.com/maintained/django-timezone-field-maintained/',
    license='BSD',
    packages=[
        'timezone_field',
    ],
    install_requires=['django>=1.6', 'pytz'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Framework :: Django',
    ],
)
