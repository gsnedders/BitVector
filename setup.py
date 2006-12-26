#!/usr/bin/env python

### setup.py

from distutils.core import setup

setup(name='BitVector',
      version='1.2',
      author='Avinash Kak',
      author_email='kak@purdue.edu',
      maintainer='Avinash Kak',
      maintainer_email='kak@purdue.edu',
      url='http://RVL4.ecn.purdue.edu/~kak/dist/BitVector-1.2.html',
      download_url='http://RVL4.ecn.purdue.edu/~kak/dist/BitVector-1.2.tar.gz?download',
      description='A pure-Python memory-efficient packed representation for bit arrays',
      long_description='''This class presents a pure-Python memory efficient packed representation for bit arrays.

      Changes introduced in version 1.2: (1) one more constructor mode: a bit vector can now be constructed directly from a bitstring; (2) rich comparison operators overloaded; (3) minimal length bit vectors constructed from int values; (4) methods provided for extending a bit vector from the left and from the right; (5) a unittest based testing framework incorporated in the package; (6) additional debugging in code and in package setup.

      Changes introduced in version 1.1.1: (1) peek feature incorporated in block reads from disk files; (2) it is now possible to construct zero-sized bit vectors.

      The class supports the following operators/methods:
      
          __getitem__

          __setitem__

          __len__

          __getslice__

          __str__

          __iter__

          __int__

          __add__

          __eq__, __ne__, __lt__, __le__, __gt__, __ge__
          

          '|'  for bitwise or

          '&'  for bitwise and

          '^'  for bitwise xor

          '~'  for bitwise inversion

          '<<' for circular shift to the left

          '>>' for circular shift to the right

          '+'  for concatenation

          intValue(), __int__  for returning the integer value 

          divide_into_two

          permute

          unpermute

          pad_from_left

          pad_from_right

          read_bits_from_file

          write_to_file

          read_bits_from_fileobject

          write_bits_to_fileobject

          ''',
      license='Python Software Foundation',
      keywords='bit array, bit vector, bit string, logical operations on bit fields',
      platforms='All platforms',
      classifiers=['Topic :: Utilities', 'Programming Language :: Python'],
      packages=['']
)
