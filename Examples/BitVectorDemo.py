#!/usr/bin/env python

import BitVector

# Construct a bit vector of size 0
bv1 = BitVector.BitVector( size = 0 )
print bv1                                   # no output

# Construct a bit vector of size 1
bv2 = BitVector.BitVector( size = 2 )
print bv2                                   # 0

# Join two bit vectors:
print bv1 + bv2                             # 0

# Construct a bit vector with a tuple of bits:
bv = BitVector.BitVector( bitlist = (1, 0, 0, 1) )
print bv                                    # 1001

# Construct a bit vector with a list of bits:    
bv = BitVector.BitVector( bitlist = [1, 1, 0, 1] )
print bv                                    # 1101

# Construct a bit vector from an integer
bv = BitVector.BitVector( intVal = 5678 )
print bv                                    # 0001011000101110
bv = BitVector.BitVector( intVal = 0 )
print bv                                    # 0
bv = BitVector.BitVector( intVal = 2 )
print bv                                    # 10
bv = BitVector.BitVector( intVal = 3 )
print bv                                    # 11
bv = BitVector.BitVector( intVal = 123456 )
print bv                                    # 11110001001000000
print bv.intValue()                         # 123456
print int( bv )

# Construct a bit vector directly from a file-like object:
import StringIO
x = "111100001111"
fp_read = StringIO.StringIO( x )
bv = BitVector.BitVector( fp = fp_read )
print bv                                    # 111100001111 

# Construct a bit vector directly from a bit string:
bv = BitVector.BitVector( bitstring = '00110011' )
print bv                                    # 00110011

bv = BitVector.BitVector( bitstring = '' )
print bv                                    # nothing

# Get the integer value of a bit vector:
print bv.intValue()                         # 51

# Test array-like indexing for a bit vector:
bv = BitVector.BitVector( bitstring = '110001' )
print bv[0], bv[1], bv[2], bv[3], bv[4], bv[5]       # 1 1 0 0 0 1
print bv[-1], bv[-2], bv[-3], bv[-4], bv[-5], bv[-6] # 1 0 0 0 1 1

# Check equality and inequality operators:
bv1 = BitVector.BitVector( bitstring = '00110011' )
bv2 = BitVector.BitVector( bitlist = [0,0,1,1,0,0,1,1] )
print bv1 == bv2                            # True
print bv1 != bv2                            # False
print bv1 < bv2                             # False
print bv1 <= bv2                            # True
bv3 = BitVector.BitVector( intVal = 5678 )
print bv3.intValue()                        # 5678
print bv3                                   # 0010110000101110
print bv1 == bv3                            # False
print bv3 > bv1                             # True
print bv3 >= bv1                            # True


# Create a string representation of a bit vector:
fp_write = StringIO.StringIO()
bv.write_bits_to_fileobject( fp_write )
print fp_write.getvalue()                   # 111100001111 

# Show array like access for getting and setting:
print bv2[2]                                # 0
bv2[2] = 1
print bv2                                   # 1111
bv2[2] = 0

# Experiments with bit-wise logical operations:
bv3 = bv1 | bv2                              
print bv3                                   # 1101
bv3 = bv1 & bv2
print bv3                                   # 1001    
bv3 = bv1 + bv2
print bv3                                   # 10011101
bv4 = BitVector.BitVector( size = 3 )
print bv4                                   # 000
bv5 = bv3 + bv4
print bv5                                   # 10011101000
bv6 = ~bv5
print bv6                                   # 01100010111
bv7 = bv5 & bv6
print bv7                                   # 00000000000
bv7 = bv5 | bv6
print bv7                                   # 11111111111

# Try setbit and getsize:
bv7[7] = 0
print bv7                                   # 11111110111
print len( bv7 )                            # 11
bv8 = (bv5 & bv6) ^ bv7
print bv8                                   # 11111110111

# Construct a bit vector from a LIST of bits:
bv = BitVector.BitVector( bitlist= [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1] )
print bv                                    # 0010010100101001

# Construct a bit vector from a file:
bv = BitVector.BitVector( filename = 'testinput1.txt' )
print bv                                    # nothing to show
bv1 = bv.read_bits_from_file(64)    
print bv1
     # 0100000100100000011010000111010101101110011001110111001001111001
bv2 = bv.read_bits_from_file(64)    
print bv2
     # 0010000001100010011100100110111101110111011011100010000001100110
bv3 = bv1 ^ (bv2)
print bv3
     # 0110000101000010000110100001101000011001000010010101001000011111

# Divide into two bit vectors:
[bv4, bv5] = bv3.divide_into_two()
print bv4                            # 01100001010000100001101000011010
print bv5                            # 00011001000010010101001000011111

# Permute a bit vector:
bv1 = BitVector.BitVector( bitlist = [1, 0, 0, 1, 1, 0, 1] )
print bv1                                    # 1001101

bv2 = bv1.permute( [6, 2, 0, 1] )
print bv2                                    # 1010
bv3 = BitVector.BitVector( bitlist = [1, 1, 0, 0, 0, 1, 1] )
print bv3                                    # 1100011
bv4 = bv1 & bv3 
print bv4                                    # 1000001
print

# Read a file from the beginning to end:
bv = BitVector.BitVector( filename = 'testinput4.txt' )
while (bv.more_to_read):
    bv_read = bv.read_bits_from_file( 64 )
    print bv_read
print

# Experiment with closing a file object and start
# extracting bit vectors from the file from
# the beginning again:
bv.close_file_object()
bv = BitVector.BitVector( filename = 'testinput4.txt' )
bv1 = bv.read_bits_from_file(64)        
print bv1           
FILEOUT = open( 'testinput5.txt', 'w' )
bv1.write_to_file( FILEOUT )
FILEOUT.close

# Experiment in 64-bit permutation and unpermutation:
# The permutation array was generated separately by the
# Fisher-Yates shuffle algorithm:
bv2 = bv1.permute( [22, 47, 33, 36, 18, 6, 32, 29, 54, 62, 4,
                    9, 42, 39, 45, 59, 8, 50, 35, 20, 25, 49,
                    15, 61, 55, 60, 0, 14, 38, 40, 23, 17, 41,
                    10, 57, 12, 30, 3, 52, 11, 26, 43, 21, 13,
                    58, 37, 48, 28, 1, 63, 2, 31, 53, 56, 44, 24,
                    51, 19, 7, 5, 34, 27, 16, 46] )
print bv2

bv3 = bv2.unpermute( [22, 47, 33, 36, 18, 6, 32, 29, 54, 62, 4,
                      9, 42, 39, 45, 59, 8, 50, 35, 20, 25, 49,
                      15, 61, 55, 60, 0, 14, 38, 40, 23, 17, 41,
                      10, 57, 12, 30, 3, 52, 11, 26, 43, 21, 13,
                      58, 37, 48, 28, 1, 63, 2, 31, 53, 56, 44, 24,
                      51, 19, 7, 5, 34, 27, 16, 46] )    
print bv3

print
print

# Try circular shifts to the left and to the right
print bv3
bv3 << 7
print bv3
bv3 >> 7
print bv3

# Test len()    
print len( bv3 )                      # 64

# Test slicing
bv4 = bv3[5:22]
print bv4                             # 00100100000011010

# Test the iterator:
for item in bv4:
    print item,                       # 0 0 1 0 0 1 0 0 0 0 0 0 1 1 0 1 0
print
    
# Demonstrate padding a bit vector from left
bv = BitVector.BitVector( bitstring = '101010' )
bv.pad_from_left( 4 )
print bv                              # 0000101010
# Demonstrate padding a bit vector from right
bv.pad_from_right( 4 )
print bv                              # 00001010100000
