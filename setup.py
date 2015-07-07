#!/usr/bin/env python

### setup.py

from distutils.core import setup

setup(name='BitVector',
      version='1.5.1',
      author='Avinash Kak',
      author_email='kak@purdue.edu',
      maintainer='Avinash Kak',
      maintainer_email='kak@purdue.edu',
      url='http://RVL4.ecn.purdue.edu/~kak/dist/BitVector-1.5.1.html',
      download_url='http://RVL4.ecn.purdue.edu/~kak/dist/BitVector-1.5.1.tar.gz?download',
      description='A pure-Python memory-efficient packed representation for bit arrays',
      long_description='''This class presents a pure-Python memory efficient packed representation for bit arrays.

Version 1.5.1 removes a crucial bug in the right circular shift operator.

Version 1.5 should prove to be much more efficient for long bit vectors.
Efficiency in BitVector construction when only its size is specified was
achieved by eliminating calls to _setbit().  The application of logical
operators to two BitVectors of equal length was also made efficient by
eliminating calls to the padding function.  Another feature of this
version is the count_bits() method that returns the total number of bits
set in a BitVector instance.  Yet another feature of this version is the
setValue() method that alters the bit pattern associated with a
previously constructed BitVector.

The class supports the following operators/methods:
      
          __getitem__

          __setitem__

          __len__

          __getslice__

          __str__

          __iter__

          __contains__

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

          slice assignment

          reset

          count_bits

          setValue

          ''',
      license='Python Software Foundation License',
      keywords='bit array, bit vector, bit string, logical operations on bit fields',
      platforms='All platforms',
      classifiers=['Topic :: Utilities', 'Programming Language :: Python'],
      packages=['']
)
