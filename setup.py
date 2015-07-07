#!/usr/bin/env python

### setup.py

from distutils.core import setup

setup(name='BitVector',
      version='1.4',
      author='Avinash Kak',
      author_email='kak@purdue.edu',
      maintainer='Avinash Kak',
      maintainer_email='kak@purdue.edu',
      url='http://RVL4.ecn.purdue.edu/~kak/dist/BitVector-1.4.html',
      download_url='http://RVL4.ecn.purdue.edu/~kak/dist/BitVector-1.4.tar.gz?download',
      description='A pure-Python memory-efficient packed representation for bit arrays',
      long_description='''This class presents a pure-Python memory efficient packed representation for bit arrays.

Version 1.4 supports slice assignment and a reset method that allows
a previously constructed bit vector to be reinitialized to all 0's 
or all 1's.  The code was also cleaned up with pychecker for this version.

In version 1.3.2, fixed a potentially misleading documentation issue for
the Windows users of the BitVector class.  If you are writing an
internally generated BitVector to a disk file, you must open the file in
the binary mode.  If you don't, the bit patterns that correspond to line
breaks will be misinterpreted.  On a Windows machine in the text mode,
the bit pattern 000001010 ('\n') will be written out to the disk as
0000110100001010 ('\r\n').

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

          ''',
      license='Python Software Foundation',
      keywords='bit array, bit vector, bit string, logical operations on bit fields',
      platforms='All platforms',
      classifiers=['Topic :: Utilities', 'Programming Language :: Python'],
      packages=['']
)
