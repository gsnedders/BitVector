#!/usr/bin/env python

import BitVector

# Construct a bit vector of size 0
print "\nConstructing a bit vector of size 0:"
bv1 = BitVector.BitVector( size = 0 )
print bv1                                   # no output

# Construct a bit vector of size 2:
print "\nConstructing a bit vector of size 2:"
bv2 = BitVector.BitVector( size = 2 )
print bv2                                   # 00

# Joining two bit vectors:
print "\nOutput concatenation of two previous bit vectors:"
print bv1 + bv2                             # 00

# Construct a bit vector with a tuple of bits:
print "\nThis is a bit vector from a tuple of bits:"
bv = BitVector.BitVector( bitlist = (1, 0, 0, 1) )
print bv                                    # 1001

# Construct a bit vector with a list of bits:    
print "\nThis is a bit vector from a list of bits:"
bv = BitVector.BitVector( bitlist = [1, 1, 0, 1] )
print bv                                    # 1101

# Construct a bit vector from an integer
bv = BitVector.BitVector( intVal = 5678 )
print "\nBit vector constructed from integer 5678:"
print bv                                    # 1011000101110
print "\nBit vector constructed from integer 0:"
bv = BitVector.BitVector( intVal = 0 )
print bv                                    # 0
print "\nBit vector constructed from integer 2:"
bv = BitVector.BitVector( intVal = 2 )
print bv                                    # 10
print "\nBit vector constructed from integer 3:"
bv = BitVector.BitVector( intVal = 3 )
print bv                                    # 11
print "\nBit vector constructed from integer 123456:"
bv = BitVector.BitVector( intVal = 123456 )
print bv                                    # 11110001001000000
print "\nInt value of the previous bit vector as computed by intVal():"
print bv.intValue()                         # 123456
print "\nInt value of the previous bit vector as computed by int():"
print int( bv )                             # 123456

# Construct a bit vector directly from a file-like object:
import StringIO
x = "111100001111"
fp_read = StringIO.StringIO( x )
bv = BitVector.BitVector( fp = fp_read )
print "\nBit vector constructed directed from a file like object:"
print bv                                    # 111100001111 

# Construct a bit vector directly from a bit string:
bv = BitVector.BitVector( bitstring = '00110011' )
print "\nBit Vector constructed directly from a string:"
print bv                                    # 00110011

bv = BitVector.BitVector( bitstring = '' )
print "\nBit Vector constructed directly from an empty string:"
print bv                                    # nothing

print "\nInteger value of the previous bit vector:"
print bv.intValue()                         # 0

# Test array-like indexing for a bit vector:
bv = BitVector.BitVector( bitstring = '110001' )
print "\nPrints out bits individually from bitstring 110001:"
print bv[0], bv[1], bv[2], bv[3], bv[4], bv[5]       # 1 1 0 0 0 1
print "\nSame as above but using negative array indexing:"
print bv[-1], bv[-2], bv[-3], bv[-4], bv[-5], bv[-6] # 1 0 0 0 1 1

# Test setting bit values with positive and negative
# accessors:
bv = BitVector.BitVector( bitstring = '1111' )
print "\nBitstring for 1111:"
print bv                                    # 1111

print "\nReset individual bits of above vector:"
bv[0]=0;bv[1]=0;bv[2]=0;bv[3]=0        
print bv                                    # 0000
print "\nDo the same as above with negative indices:"
bv[-1]=1;bv[-2]=1;bv[-4]=1
print bv                                    # 1011

print "\nCheck equality and inequality ops:"
bv1 = BitVector.BitVector( bitstring = '00110011' )
bv2 = BitVector.BitVector( bitlist = [0,0,1,1,0,0,1,1] )
print bv1 == bv2                            # True
print bv1 != bv2                            # False
print bv1 < bv2                             # False
print bv1 <= bv2                            # True
bv3 = BitVector.BitVector( intVal = 5678 )
print bv3.intValue()                        # 5678
print bv3                                   # 10110000101110
print bv1 == bv3                            # False
print bv3 > bv1                             # True
print bv3 >= bv1                            # True


# Create a string representation of a bit vector:
fp_write = StringIO.StringIO()
bv.write_bits_to_fileobject( fp_write )
print "\nGet bit vector written out to a file-like object:"
print fp_write.getvalue()                   # 1011 

print "\nExperiments with bitwise logical operations:"
bv3 = bv1 | bv2                              
print bv3                                   # 00110011
bv3 = bv1 & bv2
print bv3                                   # 00110011
bv3 = bv1 + bv2
print bv3                                   # 0011001100110011
bv4 = BitVector.BitVector( size = 3 )
print bv4                                   # 000
bv5 = bv3 + bv4
print bv5                                   # 0011001100110011000
bv6 = ~bv5
print bv6                                   # 1100110011001100111
bv7 = bv5 & bv6
print bv7                                   # 0000000000000000000
bv7 = bv5 | bv6
print bv7                                   # 1111111111111111111

print "\nTry logical operations on bit vectors of different sizes:"
print BitVector.BitVector( intVal = 6 ) ^ BitVector.BitVector( intVal = 13 )   # 1011
print BitVector.BitVector( intVal = 6 ) & BitVector.BitVector( intVal = 13 )   # 0100
print BitVector.BitVector( intVal = 6 ) | BitVector.BitVector( intVal = 13 )   # 1111

print BitVector.BitVector( intVal = 1 ) ^ BitVector.BitVector( intVal = 13 )   # 1100
print BitVector.BitVector( intVal = 1 ) & BitVector.BitVector( intVal = 13 )   # 0001
print BitVector.BitVector( intVal = 1 ) | BitVector.BitVector( intVal = 13 )   # 1101

print "\nExperiments with setbit() and getsize():"
bv7[7] = 0
print bv7                                   # 1111111011111111111
print len( bv7 )                            # 19
bv8 = (bv5 & bv6) ^ bv7
print bv8                                   # 1111111011111111111


print "\nConstruct a bit vector from what is in the file testinput1.txt:"
bv = BitVector.BitVector( filename = 'testinput1.txt' )
#print bv                                    # nothing to show
bv1 = bv.read_bits_from_file(64)    
print "\nPrint out the first 64 bits read from the file:"
print bv1
     # 0100000100100000011010000111010101101110011001110111001001111001
print "\nRead the next 64 bits from the same file:"
bv2 = bv.read_bits_from_file(64)    
print bv2
     # 0010000001100010011100100110111101110111011011100010000001100110
print "\nTake xor of the previous two bit vectors:"
bv3 = bv1 ^ (bv2)
print bv3
     # 0110000101000010000110100001101000011001000010010101001000011111


print "\nExperiment with dividing an even-sized vector into two:"
[bv4, bv5] = bv3.divide_into_two()
print bv4                            # 01100001010000100001101000011010
print bv5                            # 00011001000010010101001000011111

# Permute a bit vector:
print "\nWe will use this bit vector for experiments with permute()"
bv1 = BitVector.BitVector( bitlist = [1, 0, 0, 1, 1, 0, 1] )
print bv1                                    # 1001101

bv2 = bv1.permute( [6, 2, 0, 1] )
print "\nPermuted and contracted form of the previous bit vector:"
print bv2                                    # 1010

print "\nExperiment with writing an internally generated bit vector out to a disk file:"
bv1 = BitVector.BitVector( bitstring = '00001010' ) 
FILEOUT = open( 'test.txt', 'wb' )
bv1.write_to_file( FILEOUT )
FILEOUT.close()
bv2 = BitVector.BitVector( filename = 'test.txt' )
bv3 = bv2.read_bits_from_file( 32 )
print "\nDisplay bit vectors written out to file and read back from the file and their respective lengths:"
print bv1, bv3
print len(bv1), len(bv3)


print "\nExperiments with reading a file from the beginning to end:"
bv = BitVector.BitVector( filename = 'testinput4.txt' )
print "\nHere are all the bits read from the file:"
while (bv.more_to_read):
    bv_read = bv.read_bits_from_file( 64 )
    print bv_read
print

print "\nExperiment with closing a file object and start extracting bit vectors from the file from the beginning again:"
bv.close_file_object()
bv = BitVector.BitVector( filename = 'testinput4.txt' )
bv1 = bv.read_bits_from_file(64)        
print "\nHere are all the first 64 bits read from the file again after the file object was closed and opened again:"
print bv1           
FILEOUT = open( 'testinput5.txt', 'wb' )
bv1.write_to_file( FILEOUT )
FILEOUT.close()

print "\nExperiment in 64-bit permutation and unpermutation of the previous 64-bit bitvector:"
print "The permutation array was generated separately by the Fisher-Yates shuffle algorithm:"
bv2 = bv1.permute( [22, 47, 33, 36, 18, 6, 32, 29, 54, 62, 4,
                    9, 42, 39, 45, 59, 8, 50, 35, 20, 25, 49,
                    15, 61, 55, 60, 0, 14, 38, 40, 23, 17, 41,
                    10, 57, 12, 30, 3, 52, 11, 26, 43, 21, 13,
                    58, 37, 48, 28, 1, 63, 2, 31, 53, 56, 44, 24,
                    51, 19, 7, 5, 34, 27, 16, 46] )
print "Permuted bit vector:"
print bv2

bv3 = bv2.unpermute( [22, 47, 33, 36, 18, 6, 32, 29, 54, 62, 4,
                      9, 42, 39, 45, 59, 8, 50, 35, 20, 25, 49,
                      15, 61, 55, 60, 0, 14, 38, 40, 23, 17, 41,
                      10, 57, 12, 30, 3, 52, 11, 26, 43, 21, 13,
                      58, 37, 48, 28, 1, 63, 2, 31, 53, 56, 44, 24,
                      51, 19, 7, 5, 34, 27, 16, 46] )    
print "Unpurmute the bit vector:"
print bv3

print
print


print "\nTry circular shifts to the left and to the right for the following bit vector:"
print bv3
print "\nCircular shift to the left by 7 positions:"
bv3 << 7
print bv3
print "\nCircular shift to the right by 7 positions:"
bv3 >> 7
print bv3

print "Test len() on the above bit vector:"
print len( bv3 )                      # 64

print "\nTest forming a [5:22] slice of the above bit vector:"
bv4 = bv3[5:22]
print bv4                             # 00100100000011010

print "\nTest the iterator:"
for bit in bv4:
    print bit,                        # 0 0 1 0 0 1 0 0 0 0 0 0 1 1 0 1 0
print

print "\nDemonstrate padding a bit vector from left:"
bv = BitVector.BitVector( bitstring = '101010' )
bv.pad_from_left( 4 )
print bv                              # 0000101010
print "\nDemonstrate padding a bit vector from right:"
bv.pad_from_right( 4 )
print bv                              # 00001010100000

print "\nTest the syntax 'if bit_vector_1 in bit_vector_2' syntax:"
try:
    bv1 = BitVector.BitVector( bitstring = '0011001100' )
    bv2 = BitVector.BitVector( bitstring = '110011' )
    if bv2 in bv1:
        print "%s is in %s" % (bv2, bv1)
    else:
        print "%s is not in %s" % (bv2, bv1)
except ValueError, arg:
    print "Error Message: " + str(arg)

print "\nTest the size modifier when a bit vector is initialized with the intVal method:"
bv = BitVector.BitVector( intVal = 45, size = 16 )
print bv                              # 0000000000101101
bv = BitVector.BitVector( intVal = 0, size = 8 )    
print bv                              # 00000000
bv = BitVector.BitVector( intVal = 1, size = 8 )    
print bv                              # 00000001

print "\nTesting slice assignment:"
bv1 = BitVector.BitVector( size = 25 )
print "bv1= ", bv1                    # 0000000000000000000000000
bv2 = BitVector.BitVector( bitstring = '1010001' )
print "bv2= ", bv2                    # 1010001  
bv1[6:9]  = bv2[0:3]
print "bv1= ", bv1                    # 0000001010000000000000000

print "\nTesting reset function:"
bv1.reset( 1 )
print "bv1= ", bv1                    # 1111111111111111111111111
print bv1[3:9].reset(0)               # 000000
print bv1[:].reset(0)                 # 0000000000000000000000000

print "\nTesting count_bit():"
bv = BitVector.BitVector( intVal = 45, size = 16 )
y = bv.count_bits()
print y                               # 4     
bv = BitVector.BitVector( bitstring = '100111' )
print bv.count_bits()                 # 4
bv = BitVector.BitVector( bitstring = '00111000' )
print bv.count_bits()                 # 3
bv = BitVector.BitVector( bitstring = '001' )
print bv.count_bits()                 # 1
bv = BitVector.BitVector( bitstring = '00000000000000' )
print bv.count_bits()                 # 0

print "\nTest setValue idea:"
bv = BitVector.BitVector( intVal = 7, size =16 )
print bv                              # 0000000000000111
bv.setValue( intVal = 45 )
print bv                              # 101101


