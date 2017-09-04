import os

from setuptools import find_packages, setup

setup(name='snakify',
      version='1.1.1',
      description=("Slugify a string to a valid Python variable name."),
      #long_description=open('README.rst').read(),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'
                    ],
      keywords='serialization slugification',
      author='Stijn Debrouwere',
      author_email='stijn@debrouwere.org',
      download_url='http://www.github.com/debrouwere/python-snakify/tarball/master',
      license='ISC',
      test_suite='snakify.tests',
      packages=find_packages(),
      install_requires=[
        'num2words>=0.5.4',
        'unicode-slugify>=0.1.3',
        ]
      )
