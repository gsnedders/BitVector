#!/usr/bin/env python

### setup.py

from distutils.core import setup

setup(name='BitVector',
      version='2.0.1',
      author='Avinash Kak',
      author_email='kak@purdue.edu',
      maintainer='Avinash Kak',
      maintainer_email='kak@purdue.edu',
      url='http://RVL4.ecn.purdue.edu/~kak/dist/BitVector-2.0.1.html',
      download_url='http://RVL4.ecn.purdue.edu/~kak/dist/BitVector-2.0.1.tar.gz?download',
      description='A pure-Python memory-efficient packed representation for bit arrays',
      long_description='''
This class presents a pure-Python memory efficient packed 
representation for bit arrays.

Version 2.0.1 removes many typos and other errors in the 
documentation page.  The implementation code remains 
the same as in Version 2.0

Version 2.0 provides much additional functionality that was
requested by folks in the data mining community.  The class
now includes faster methods for counting bits, for finding
the position of the next set bit, for calculating the rank
of a bit, for determining the Jaccard and Hamming distances,
etc.  Also included in the new version are methods that
should prove useful to folks who play with cryptography
algorithms.  There is now a method that calculates the
greatest common divisor of two bit vectors and a method that
finds the multiplicative inverse of a bit vector vis-a-vis a
given modulus.

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

          setValue

          count_bits

          count_bit_sparse          
 
          jaccard_similarity

          jaccard_distance

          hamming_distance

          next_set_bit

          rank_of_bit_set_at_index

          isPowerOf2

          isPowerOf2_sparse

          reverse

          gcd

          multiplicative_inverse

          ''',
      license='Python Software Foundation License',
      keywords='bit array, bit vector, bit string, logical operations on bit fields',
      platforms='All platforms',
      classifiers=['Topic :: Utilities', 'Programming Language :: Python'],
      packages=['']
)
