#!/usr/bin/python

import sys
from distutils.core import setup


def main():
    if not sys.version.startswith('2.'):
        sys.stderr.write('This backport is for Python 2.x only.\n')
        sys.exit(1)

    setup(
      name='functools32',
      version='3.2.3',
      description='Backport of the functools module from Python 3.2.3 for use on 2.x.',
      long_description="""
This is a backport of the functools standard library module from
Python 3.2.3 for use on Python 2.4, 2.5, 2.6 and 2.7. It includes
new features `lru_cache` (Least-recently-used cache decorator).""",
      license='PSF license',

      maintainer='ENDOH takanao',
      maintainer_email='djmchl@gmail.com',
      url='https://github.com/MiCHiLU/python-functools32',

      py_modules=['functools32'],
    )


if __name__ == '__main__':
    main()
