#!/usr/local/bin/python

### setup.py

from distutils.core import setup

setup(name='BitVector',
      version='1.1',
      author='Avinash Kak',
      author_email='kak@purdue.edu',
      maintainer='Avinash Kak',
      maintainer_email='kak@purdue.edu',
      url='http://RVL4.ecn.purdue.edu/dist/BitVector-1.1.html',
      download_url='http://RVL4.ecn.purdue.edu/dist/?action=AttachFile&do=get&target=BitVector-1.1.tar.gz',
      description='A pure-Python memory-efficient packed representation for bit arrays',
      long_description='''This class presents a pure-Python memory efficient packed representation for bit arrays. The class supports the following methods:
          __getitem__
          __setitem__
          __len__
          __getslice__
          __str__
          __iter__
          '|'  for bitwise or
          '&'  for bitwise and
          '^'  for bitwise xor
          '~'  for bitwise inversion
          '<<' for circular shift to the left
          '>>' for circular shift to the right
          '+'  for concatenation
          divide_into_two
          permute
          unpermute
          read_bits_from_file
          write_to_file
          read_bits_from_fileobject
          write_bits_to_fileobject
          ''',
      license='Python Software Foundation',
      keywords='bit array, bit vector, bit string, logical operations on bit fields',
      platforms='All platforms',
      classifiers=['Topic :: Utilities', 'Programming Language :: Python'],
)
