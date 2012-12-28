#!/usr/bin/env python

### setup.py

from distutils.core import setup

setup(name='BitVector',
      version='3.2',
      author='Avinash Kak',
      author_email='kak@purdue.edu',
      maintainer='Avinash Kak',
      maintainer_email='kak@purdue.edu',
      url='https://engineering.purdue.edu/kak/dist/BitVector-3.2.html',
      download_url='https://engineering.purdue.edu/kak/dist/BitVector-3.2.tar.gz?download',
      description='A pure-Python memory-efficient packed representation for bit arrays',
      long_description='''
This class presents a pure-Python memory-efficient packed 
representation for bit arrays.

**Version 3.2** includes support for constructing bit
vectors directly from text strings and hex strings.

**Version 3.1.1** removes the incompatibility of the module
test code with how Python 2.7 expects its string input for
creating memory files. **This version of the module should
work with all recent versions of Python 2.x and with Python
3.x.**

**Version 3.1** includes a documentation error fix, a bug
fix in the slice assignment code, and two new methods useful
for security work.

The class is provided with the following operators/methods:

-      __getitem__
-      __setitem__
-      __len__
-      __iter__
-      __contains__
-      __getslice__
-      __str__
-      __int__
-      __add__
-      __eq__, __ne__, __lt__, __le__, __gt__, __ge__
-      __or__
-      __and__
-      __xor__
-      __invert__
-      __lshift__
-      __rshift__
-      __add__
-      count_bits 
-      count_bits_sparse      (faster for sparse bit vectors)     
-      deep_copy
-      divide_into_two
-      gcd
-      gen_rand_bits_for_prime
-      getHexStringFromBitVector
-      getTextFromBitVector
-      gf_divide              (for divisions in GF(2^n))
-      gf_MI                  (for multiplicative inverse in GF(2^n))
-      gf_multiply            (for multiplications in GF(2))
-      gf_multiply_modular    (for multiplications in GF(2^n))
-      hamming_distance
-      intValue               (for returning the integer value) 
-      isPowerOf2
-      isPowerOf2_sparse      (faster for sparse bit vectors)
-      jaccard_distance
-      jaccard_similarity
-      length                 
-      multiplicative_inverse
-      next_set_bit
-      pad_from_left
-      pad_from_right
-      permute
-      rank_of_bit_set_at_index
-      read_bits_from_file
-      reset
-      reverse
-      runs
-      shift_left             for non-circular left shift
-      shift_right            for non-circular right shift
-      slice assignment
-      setValue
-      test_for_primality
-      unpermute
-      write_to_file
-      write_bits_to_fileobject

          ''',
      license='Python Software Foundation License',
      keywords='bit array, bit vector, bit string, logical operations on bit fields',
      platforms='All platforms',
      classifiers=['Topic :: Utilities', 'Programming Language :: Python'],
      packages=['']
)
