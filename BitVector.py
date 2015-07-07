#!/usr/local/bin/python


'''
   BitVector.py        

   Version: 1.1.1
   
   Author: Avinash Kak (kak@purdue.edu)


   CHANGE LOG:

       Version 1.1.1: The function that does block reads from a disk
       file now peeks ahead at the end of each block to see if there is
       anything remaining to be read in the file.  If nothing remains,
       the more_to_read attribute of the BitVector object is set to
       False.  This simplifies reading loops. This version also allows
       BitVectors of size 0 to be constructed


       Version 1.1: I have changed the API significantly to provide
       more ways for constructing a bit vector.  As a result, it is
       now necessary to supply a keyword argument to the constructor.
       

   INTRODUCTION:
   
   The BitVector class for a memory-efficient packed representation of
   bit arrays and for logical operations on such arrays.  The core idea
   used in this Python script for bin packing is based on an internet
   posting by Josiah Carlson to the Pyrex mailing list.

   Operations Supported on bit vectors:

              __getitem__
              __setitem__
              __len__
              __iter__
              __getslice__
              __str__
              |       for bitwise or
              &       for bitwise and              
              ^       for bitwise xor
              ~       for bitwise inversion
              <<      for circular rotation to the left
              >>      for circular rotation to the right
              +       for concatenation
              divide_into_two
              permute
              unpermute
              read_bits_from_file
              write_to_file
              read_bits_from_fileobject
              write_bits_to_fileobject



   CONSTRUCTING BIT VECTORS:

   You can construct a bit vector in five different ways.
   
   (1) You can construct a bit vector directly from either a tuple or
       a list of bits, as in

          bv =  BitVector( bits = [1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1] )   

   (2) You can construct a bit vector from an integer by

          bv =  BitVector( intVal = 56789 )

       The bits stored now will correspond to the binary representation of
       the integer.

   (3) You can create a zero-initialized bit vector of a given size
       by

          bv  = BitVector( size = 62 )

       This bit vector will hold exactly 62 bits, all initialized to the
       0 bit value.

   (4) You can construct a bit vector from a disk file by a two-step
       procedure. First you construct an instance of bit vector by
   
          bv  =  BitVector( filename = 'somefile' )   

       This bit vector itself is incapable of holding the bits.  To
       now create bit vectors that actually hold the bits, you need
       to make the following sort of a call on the above variable bv:
 
          bv1 =  bv.read_bits_from_file( 64 )    

       bv1 will be a regular bit vector containing 64 bits from the disk
       file. If you want to re-read a file from the beginning for some
       reason, you must obviously first close the file object that was
       acquired with a call to the BitVector constructor with a filename
       argument.  This can be accomplished by

          bv.close_file_object()

   (5) Yet another way to construct a bit vector is to read the bits
       directly from a file-like object, as in

          x = "111100001111"
          fileobj = StringIO.StringIO( x )
          bv = BitVector( fp = fileobj )


   

   DISPLAYING BIT VECTORS:

   Since the BitVector class implements the __str__ method, a
   bit vector can be displayed on a terminal by

          print bitvec



   ACCESSING AND SETTING INDIVIDUAL BITS AND SLICES:
   
   Any single bit of a bit vector bv can be set to 1 or 0 by

          bv[M] = 1_or_0
          print bv[M]

   for accessing (and setting) the bit at the position that is
   indexed M.  You can retrieve the bit at position M by bv[M].

   A slice of a bit vector obtained by

          bv[i:j]

   is a bit vector constructed from the bits at index positions
   from i through j-1.

   You can iterate over a bit vector, as illustrated by

          for item in bitvec:
              print item,   
   



   LOGICAL OPERATIONS ON BIT VECTORS:
   
   Given two bit vectors bv1 and bv2, you can perform bitwise
   logical operations on them by

           result_bv  =  bv1 ^ bv2
           result_bv  =  bv1 & bv2
           result_bv  =  bv1 | bv2
           result_bv  =  ~bv1



   OTHER SUPPORTED OPERATIONS:
   
   Additional operations supported on bit vectors are

           bv_permuted     =  bv.permute( permutation_list )

           bv_unpermuted   =  bv.unpermute( permutation_list )
 
   The BitVector class also supports the following circular shift
   operations:

            bitvec  << N 

            bitvec  >> N

   for circular rotations to the left and right by N bit positions.
   A bit vector containing an even number of bits can be divided into
   two equal parts by

       [left_half, right_half] = bitvec.divide_into_two()

   where left_half and right_half hold references to the two returned
   bit vectors.



   HOW THE BIT VECTORS ARE STORED:
   
   The bits of a bit array are stored in 16-bit unsigned ints.  After
   resolving the argument with which the constructor is called (which
   happens in lines (A2) through (A46)), the very first thing that the
   constructor does is to figure out in line (A47) as to how many of
   those 2-byte ints it needs for the bits.  For example, if you wanted
   to store a 64-bit array, the variable 'two_byte_ints_needed' in line
   (A47) would be set to 4. (This does not mean that the size of a bit
   vector must be a multiple of 16.  Any sized bit vectors can
   constructed using the required number of two-byte ints.) Line (A48)
   then creates an array of 2-byte ints and initializes it with the
   required number of zeros.  Lines (A49) then shifts the bits into the
   array of two-byte ints.

   As mentioned above, note that it is not necessary for the size of the
   vector to be a multiple of 16 even though we are using C's unsigned
   short as as a basic unit for storing the bit arrays.  The class
   BitVector keeps track of the actual number of bits in the bit vector
   through the "size" instance attribute.

   With regard to the code in lines (A2) through (A46), note that
   the constructor must be called with a single keyword argument,
   which determines how the bit vector will be constructed.
   Lines (A10) through (A17) are for the following sort of a call

          bv = BitVector( filename = 'myfilename' )

   This calls returns a bit vector on which you must subsequently
   invoke the 'read_bits_from_file' method to actually obtain a
   bit vector consisting of the bits that constitute the information
   stored in the file.  Lines (A18) through (A23) are for the case
   when you want to construct a bit vector by reading the bits off
   a file-like object, as in

          x = "111100001111"
          fileobj = StringIO.StringIO( x )
          bv = BitVector( fp = fileobj )

   Lines (A24) through (A28) are for constructing a bit vector with
   just the size information, as in

       bv = BitVector( size = 61 )

   This returns a bit vector that will hold exactly 61 bits, all
   initialized to the zero value.  Lines (A29) through (A40) are
   for the case when you want to construct a bit vector from
   an integer, as in

          bv = BitVector( intVal = 123456 )

   The bits stored in the bit vector will correspond to the binary
   representation of the integer argument provided. Finally, lines
   (A41) through (A44) are for the following direct approach to the
   construction of a bit vector:
          
          bv = BitVector( bits = (1, 0, 1, 1, 0, 0, 1) )

   Now the bit vector constructed will be initialized at the same
   time with the supplied bits.

   

   ACKNOWLEDGEMENTS

   The author is grateful to Oleg Broytmann for suggesting many
   improvements that have now been incorporated in this version of the
   BitVector class.  The author would also like to thank all (Scott
   Daniels, Blair Houghton, and Steven D'Aprano) for their responses to
   my comp.lang.python query concerning how to make a Python input
   stream peekable.
   
'''


import sys
import array
import exceptions
import operator

_hexdict = { '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
             '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
             '8' : '1000', '9' : '1001', 'a' : '1010', 'b' : '1011',
             'c' : '1100', 'd' : '1101', 'e' : '1110', 'f' : '1111' }

# If this function can read all blocksize bits, it peeks ahead
# to see if there is anything more to be read in the file. It
# uses tell-read-seek mechanism for this in lines (R17) through
# (R19).  If there is nothing further to be read, it sets the
# more_to_read attribute of the bitvector object to False.
# Obviously, this can only be done for seekable streams such
# as those connected with disk files.  According to Blair Houghton,
# a similar feature could presumably be implemented for socket
# streams by using recv() or recvfrom() if you set the flags
# argument to MSG_PEEK. 
def _readblock( blocksize, bitvector ):                              #(R1)
    global hexdict                                                   #(R2)
    bitstring = ''                                                   #(R3)
    i = 0                                                            #(R4)
    while ( i < blocksize / 8 ):                                     #(R5)
        i += 1                                                       #(R6)
        byte = bitvector.FILEIN.read(1)                              #(R7)
        if byte == '':                                               #(R8)
            if len(bitstring) < blocksize:
                bitvector.more_to_read = False
            return bitstring                                         #(R9)
        hexvalue = hex( ord( byte ) )                               #(R10)
        hexvalue = hexvalue[2:]                                     #(R11)
        if len( hexvalue ) == 1:                                    #(R12)
            hexvalue = '0' + hexvalue                               #(R13)
        bitstring += _hexdict[ hexvalue[0] ]                        #(R14)
        bitstring += _hexdict[ hexvalue[1] ]                        #(R15)
    file_pos = bitvector.FILEIN.tell()                              #(R16)
    # peek at the next byte; moves file position only if a
    # byte is read
    next_byte = bitvector.FILEIN.read(1)                            #(R17)
    if next_byte:                                                   #(R18)
        # pretend we never read the byte                   
        bitvector.FILEIN.seek( file_pos )                           #(R19)
    else:                                                           #(R20)
        bitvector.more_to_read = False                              #(R21)
    return bitstring                                                #(R22)


class BitVector( object ):                                           #(A1)

    def __init__( self, *args, **kwargs ):                           #(A2)
        if args:                                                     #(A3)
               raise ValueError(
                      '''BitVector constructor can only be called
                         with keyword arguments for the following
                         keywords: filename, fp (for fileobject),
                         size, intValue, or bits (for a tuple of
                         bits)''')
        filename = fp = size = intVal = bits = None                  #(A4)
        if kwargs.has_key('filename'):filename=kwargs.pop('filename')#(A5)
        if kwargs.has_key('fp'):           fp = kwargs.pop('fp')     #(A6)
        if kwargs.has_key('size'):       size = kwargs.pop('size')   #(A7)
        if kwargs.has_key('intVal'):   intVal = kwargs.pop('intVal') #(A8)
        if kwargs.has_key('bits'):       bits = kwargs.pop('bits')   #(A9)

        if filename:                                                #(A10)
            if fp or size or intVal or bits:                        #(A11)
                raise ValueError(                                   #(A12)
                  '''When filename is specified, you cannot
                     give values to any other constructor args''')
            self.filename = filename                                #(A13)
            self.FILEIN = open( filename, 'rb' )                    #(A14)
            self.size = 0                                           #(A15)
            self.more_to_read = True                                #(A16)
            return                                                  #(A17)
        elif fp:                                                    #(A18)
            if filename or size or intVal or bits:                  #(A19)
                raise ValueError(                                   #(A20)
                  '''When fileobject is specified, you cannot       
                     give values to any other constructor args''')
            bits = self.read_bits_from_fileobject( fp )             #(A21)
            bits =  map( lambda x: int(x), bits )                   #(A22)
            self.size = len( bits )                                 #(A23)
        elif size >= 0:                                             #(A24)
            if filename or fp or intVal or bits:                    #(A25)
                raise ValueError(                                   #(A26)
                  '''When size is specified, you cannot
                     give values to any other constructor args''')
            self.size = size                                        #(A27)
            bits = tuple( [0] * size )                              #(A28)
        elif intVal:                                                #(A29)
            if filename or fp or size or bits:                      #(A30)
                raise ValueError(                                   #(A31)
                  '''When intVal is specified, you cannot
                     give values to any other constructor args''')
            hexVal = hex( intVal )                                  #(A32)
            hexVal = hexVal[2:]                                     #(A33)
            if len( hexVal ) == 1:                                  #(A34)
                hexVal = '0' + hexVal                               #(A35)
            bits = []                                               #(A36)
            for item in hexVal[:]:                                  #(A37)
                bits += _hexdict[item][:]                           #(A38)
            bits =  map( lambda x: int(x), bits )                   #(A39)
            self.size = len( bits )                                 #(A40)
        elif bits:                                                  #(A41)
            if filename or fp or size or intVal:                    #(A42)
                raise ValueError(                                   #(A43)
                  '''When bits are specified, you cannot
                     give values to any other constructor args''')
            self.size = len( bits )                                 #(A44)
        else:                                                       #(A45)
            raise ValueError("wrong arg(s) for constructor")        #(A46) 
        two_byte_ints_needed = (len(bits) + 15) // 16               #(A47)
        self.vector = array.array( 'H', [0]*two_byte_ints_needed )  #(A48)
        map( self._setbit, enumerate(bits), bits)                   #(A49)

    # Set the bit at the designated position to the value shown:
    def _setbit( self, posn, val ):                                  #(B1)
        if val not in (0, 1):                                        #(B2)
            raise ValueError( "incorrect value for a bit" )          #(B3)
        if isinstance( posn, (tuple) ):                              #(B4)
            posn = posn[0]                                           #(B5)
        if posn >= self.size:                                        #(B6)
            raise exceptions.ValueError, "index range error"         #(B7)   
        block_index = posn // 16                                     #(B8)
        shift = posn & 15                                            #(B9)
        cv = self.vector[block_index]                               #(B10)
        if ( cv >> shift ) & 1 != val:                              #(B11)
            self.vector[block_index] = cv ^ (1 << shift)            #(B12)

    # Get the bit from the designated position:
    def _getbit( self, posn ):                                       #(C1)
        if posn >= self.size:                                        #(C2)
            raise ValueError( "index range error" )                  #(C3)   
        return ( self.vector[posn//16] >> (posn&15) ) & 1            #(C4)

    # Take a bitwise 'xor' of the bit vector on which the method is
    # invoked with the argument bit vector.  Return the result as
    # a new bit vector:
    def __xor__(self, other):                                        #(E1)
        if self.size != other.size:                                  #(E2)
            raise AttributeError( "bitvecs unequal in size" )        #(E3)
        res = BitVector( size = self.size )                          #(E4)
        res.vector = map(operator.__xor__, self.vector, other.vector)#(E5) 
        return res                                                   #(E6)

    # Take a bitwise 'and' of the bit vector on which the method is
    # invoked with the argument bit vector.  Return the result as
    # a new bit vector:
    def __and__(self, other):                                        #(F1)
        if self.size != other.size:                                  #(F2)
            raise AttributeError( "bitvecs unequal in size" )        #(F3)
        res = BitVector( size = self.size )                          #(F4)
        res.vector = map(operator.__and__, self.vector, other.vector)#(F5)
        return res                                                   #(F6)

    # Take a bitwise 'or' of the bit vector on which the method is
    # invoked with the argument bit vector.  Return the result as
    # a new bit vector:
    def __or__(self, other):                                         #(G1)
        if self.size != other.size:                                  #(G2)
            raise AttributeError( "bitvecs unequal in size" )        #(G3)
        res = BitVector( size = self.size )                          #(G4)
        res.vector = map( operator.__or__, self.vector, other.vector)#(G5)
        return res                                                   #(G6)

    # Invert the bits in the bit vector on which the method is
    # invoked and return the result as a new bit vector:
    def __invert__(self):                                            #(H1)
        res = BitVector( size = self.size )                          #(H2)
        res.vector = map( operator.__inv__, self.vector )            #(H3)
        return res                                                   #(H4)

    # Concatenate the argument bit vector with the bit vector
    # on which the method is invoked.  Return the concatenated
    # bit vector as a new BitVector object:
    def __add__(self, other):                                        #(J1)
        i = 0                                                        #(J2)
        outlist = []                                                 #(J3)
        while ( i < self.size ):                                     #(J4)
            outlist.append( self[i] )                                #(J5)
            i += 1                                                   #(J6)
        i = 0                                                        #(J7)
        while ( i < other.size ):                                    #(J8)
            outlist.append( other[i] )                               #(J9)
            i += 1                                                  #(J10)
        return BitVector( bits = outlist )                          #(J11)

    # Return the number of bits in a bit vector:
    def _getsize(self):                                              #(K1)
        return self.size                                             #(K2)

    # Read blocksize bits from a disk file and return a
    # BitVector object containing the bits.  If the file
    # contains fewer bits than blocksize, construct the
    # BitVector object from however many bits there are
    # in the file.  If the file contains zero bits, return
    # a BitVector object of size attribute set to 0.
    def read_bits_from_file(self, blocksize):                        #(L1)
        error_str = '''You need to first construct a BitVector
        object with a filename as  argument'''                       #(L2)
        if self.filename == None:                                    #(L3)
            raise SyntaxError( error_str )                           #(L4)
        if blocksize % 8 != 0:                                       #(L5)
            raise ValueError( "block size must be a multiple of 8" ) #(L6)
        bitstring = _readblock( blocksize, self )                    #(L7)
        if len( bitstring ) == 0:                                    #(L8)
            return BitVector( size = 0 )                             #(L9)
        else:                                                       #(L10)
            bitlist = map( lambda x: int(x), list( bitstring ) )    #(L11)
            return BitVector( bits = bitlist )                      #(L12)

    # This function is meant to read a bit string from a
    # file like object.
    def read_bits_from_fileobject( self, fp ):                       #(M1)
        bits = []                                                    #(M2)
        while True:                                                  #(M3)
            bit = fp.read()                                          #(M4)
            if bit == '': return bits                                #(M5)
            bits += bit                                              #(M6)

    # This function is meant to write a bit vector directly to
    # a file like object.  Note that whereas 'write_to_file'
    # method creates a memory footprint that corresponds exactly
    # to the bit vector, the 'write_bits_to_fileobject' actually
    # writes out the 1's and 0's as individual items to the
    # file object.  That makes this method convenient for
    # creating a string representation of a bit vector,
    # especially if you use the StringIO class, as shown in
    # the test code.
    def write_bits_to_fileobject( self, fp ):                        #(N1)
        for bit_index in range(self.size):                           #(N2)
            if self[bit_index] == 0:                                 #(N3)
                fp.write( '0' )                                      #(N4)
            else:                                                    #(N5)
                fp.write( '1' )                                      #(N6)

    # Divides an even-sized bit vector into two and returns
    # the two halves as a list of two bit vectors.
    def divide_into_two(self):                                       #(P1)
        if self.size % 2 != 0:                                       #(P2)
            raise ValueError( "must have even num bits" )            #(P3)
        i = 0                                                        #(P4)
        outlist1 = []                                                #(P5)
        while ( i < self.size /2 ):                                  #(P6)
            outlist1.append( self[i] )                               #(P7)
            i += 1                                                   #(P8)
        outlist2 = []                                                #(P9)
        while ( i < self.size ):                                    #(P10)
            outlist2.append( self[i] )                              #(P11)
            i += 1                                                  #(P12)
        return [ BitVector( bits = outlist1 ),
                 BitVector( bits = outlist2 ) ]                     #(P13)

    # Permute a bit vector according to the indices shown in the
    # second argument list.  Return the permuted bit vector as a
    # new bit vector.
    def permute(self, permute_list):                                 #(Q1)
        if max(permute_list) > self.size -1:                         #(Q2)
            raise ValueError( "Bad permutation index" )              #(Q3)
        outlist = []                                                 #(Q4)
        i = 0                                                        #(Q5)
        while ( i < len( permute_list ) ):                           #(Q6)
            outlist.append( self[ permute_list[i] ] )                #(Q7)
            i += 1                                                   #(Q8)
        return BitVector( bits = outlist )                           #(Q9)

    # Unpermute the bit vector according to the permutation list
    # supplied as the second argument.  If you first permute a
    # bit vector by using permute() and then unpermute() it using
    # the same permutation list, you will get back the original bit
    # vector.
    def unpermute(self, permute_list):                               #(S1)
        if max(permute_list) > self.size -1:                         #(S2)
            raise exceptions.ValueError, "Bad permutation index"     #(S3)
        if self.size != len( permute_list ):                         #(S4)
            raise exceptions.ValueError,"Bad size for permute list"  #(S5)
        out_bv = BitVector( size = self.size )                       #(S6)
        i = 0                                                        #(S7)
        while ( i < len(permute_list) ):                             #(S8)
            out_bv[ permute_list[i] ] = self[i]                      #(S9)
            i += 1                                                  #(S10)
        return out_bv                                               #(S11)

    # Contributed by Joe Davidson
    # Write the bitvector to the file object file_out.           
    # (A file object is returned by a call to open()).           
    # Hopefully the bitvector is a multiple of 8 bits ...
    # Each byte treated as MSB first (0th index)
    def write_to_file(self, file_out):                               #(T1)
        for byte in range(self.size/8 ):                             #(T2)
            value = 0                                                #(T3)
            for bit in range(8):                                     #(T4)
                value += (self._getbit( byte*8 + (7 - bit) ) << bit )#(T5)
            file_out.write( chr(value) )                             #(T6)

    # For closing a file object that was used for reading
    # the bits into one or more BitVector objects
    def close_file_object(self):                                     #(U1)
        if self.filename == None:                                    #(U2)
            raise exceptions.SyntaxError, "No associated open file"  #(U3)
        self.FILEIN.close()                                          #(U4)

    # For an in-place left circular shift by n bit positions:
    def __lshift__( self, n ):                                       #(V1)
        for i in range(n):                                           #(V2)
            self.circular_rotate_left_by_one()                       #(V3)

    # For an in-place right circular shift by n bit positions:
    def __rshift__( self, n ):                                       #(W1)
        for i in range(n):                                           #(W2)
            self.circular_rotate_right_by_one()                      #(W3)

    # For a one-bit in-place left circular shift:
    def circular_rotate_left_by_one(self):                           #(X1)
        size = len(self.vector)                                      #(X2)
        bitstring_leftmost_bit = self.vector[0] & 1                  #(X3)
        left_most_bits = map(operator.__and__, self.vector, [1]*size)#(X4)
        left_most_bits.append(left_most_bits[0])                     #(X5)
        del(left_most_bits[0])                                       #(X6)
        self.vector = map(operator.__rshift__, self.vector, [1]*size)#(X7)
        self.vector = map( operator.__or__, self.vector, \
             map(operator.__lshift__, left_most_bits, [15]*size) )   #(X8)
        self._setbit(self.size -1, bitstring_leftmost_bit)           #(X9)

    # For a one-bit in-place right circular shift:
    def circular_rotate_right_by_one(self):                          #(Y1)
        size = len(self.vector)                                      #(Y2)
        bitstring_rightmost_bit = self[self.size - 1]                #(Y3)
        right_most_bits = map( operator.__and__,
                               self.vector, [0x8000]*size )          #(Y4)
        map( operator.__and__, self.vector, [~0x8000]*size )         #(Y5)
        right_most_bits.insert(0, bitstring_rightmost_bit)           #(Y6)
        right_most_bits.pop()                                        #(Y7)
        self.vector = map(operator.__lshift__, self.vector, [1]*size)#(Y8)
        self.vector = map( operator.__or__, self.vector, \
             map(operator.__rshift__, right_most_bits, [15]*size) )  #(Y9)
        self._setbit(0, bitstring_rightmost_bit)                    #(Y10)

    # This is merely another implementation of the method
    # circular_rotate_left_by_one() shown above.  This one
    # does NOT use map functions.  This method carries out a
    # one-bit left circular shift of a bit vector.
    def circular_rot_left(self):                                     #(Z1)
        max_index = (self.size -1)  // 16                            #(Z2)
        left_most_bit = self.vector[0] & 1                           #(Z3)
        self.vector[0] = self.vector[0] >> 1                         #(Z4)
        for i in range(1, max_index + 1):                            #(Z5)
            left_bit = self.vector[i] & 1                            #(Z6)
            self.vector[i] = self.vector[i] >> 1                     #(Z7)
            self.vector[i-1] |= left_bit << 15                       #(Z8)
        self._setbit(self.size -1, left_most_bit)                    #(Z9)

    # This is merely another implementation of the method
    # circular_rotate_right_by_one() shown above.  This one
    # does NOT use map functions.  This method does a one-bit
    # right circular shift of a bit vector.
    def circular_rot_right(self):                                    #(a1)
        max_index = (self.size -1)  // 16                            #(a2)
        right_most_bit = self[self.size - 1]                         #(a3)
        self.vector[max_index] &= ~0x8000                            #(a4)
        self.vector[max_index] = self.vector[max_index] << 1         #(a5)
        for i in range(max_index-1, -1, -1):                         #(a6)
            right_bit = self.vector[i] & 0x8000                      #(a7)
            self.vector[i] &= ~0x8000                                #(a8)
            self.vector[i] = self.vector[i] << 1                     #(a9)
            self.vector[i+1] |= right_bit >> 15                     #(a10)
        self._setbit(0, right_most_bit)                             #(a11)


    # Allow array like subscripting for getting and setting:
    __getitem__ = _getbit                                            #(b1)
    __setitem__ = _setbit                                            #(b2)

    # Allow slicing with [i:j], [:], etc.
    def __getslice__(self, i, j):                                    #(c1)
        slicebits = []                                               #(c2)
        if j > self.size: j = self.size                              #(c3)
        for x in range(i,j):                                         #(c4)
            slicebits.append( self[x] )                              #(c5)
        return BitVector( bits = slicebits )                         #(c6)

    # Allow len() to work:
    __len__ = _getsize                                               #(d1)

    # To allow iterations over a bit vector:
    def __iter__( self ):                                            #(e1)
        return BitVectorIterator( self )                             #(e2)

    # To create a print representation
    def __str__( self ):                                             #(f1)
        if self.size == 0:                                           #(f2)
            return ''                                                #(f3)
        return ''.join( map( lambda x: str(x), self ) )              #(f4)

class BitVectorIterator:                                             #(g1)
    def __init__( self, bitvec ):                                    #(g2)
        self.items = bitvec[:]                                       #(g3)
        self.index = -1                                              #(g4)

    def __iter__( self ):                                            #(g5)
        return self                                                  #(g6)

    def next( self ):                                                #(g7)
        self.index += 1                                              #(g8)
        if self.index < len( self.items ):                           #(g9)
            return self.items[ self.index ]                         #(g10)
        else:                                                       #(q11)
            raise StopIteration                                     #(g12)

       
#------------------------  End of Class Definition -----------------------

#------------------------     Test Code Follows    -----------------------

if __name__ == '__main__':

    # Construct a bit vector with a tuple of bits:
    bv1 = BitVector( bits = (1, 0, 0, 1) )
    print bv1                                   # 1001

    # Construct a bit vector with a list of bits:    
    bv2 = BitVector( bits = [1, 1, 0, 1] )
    print bv2                                   # 1101

    # Construct a bit vector from an integer
    bv = BitVector( intVal = 5678 )
    print bv                                    # 0001011000101110

    # Construct a bit vector directly from a file-like object:
    import StringIO
    x = "111100001111"
    fp_read = StringIO.StringIO( x )
    bv = BitVector( fp = fp_read )
    print bv                                    # 111100001111 
    
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
    bv4 = BitVector( size = 3 )
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
    bv = BitVector( bits= [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1] )
    print bv                                    # 0010010100101001

    # Construct a bit vector from a file:
    bv = BitVector( filename = 'junk.txt' )
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
    bv1 = BitVector( bits = [1, 0, 0, 1, 1, 0, 1] )
    print bv1                                    # 1001101
    
    bv2 = bv1.permute( [6, 2, 0, 1] )
    print bv2                                    # 1010
    bv3 = BitVector( bits = [1, 1, 0, 0, 0, 1, 1] )
    print bv3                                    # 1100011
    bv4 = bv1 & bv3 
    print bv4                                    # 1000001
    print

    # Read a file from the beginning to end:
    bv = BitVector( filename = 'junk4.txt' )
    while (bv.more_to_read):
        bv_read = bv.read_bits_from_file( 64 )
        print bv_read
    print

    # Experiment with closing a file object and start
    # extracting bit vectors from the file from
    # the beginning again:
    bv.close_file_object()
    bv = BitVector( filename = 'junk3.txt' )
    bv1 = bv.read_bits_from_file(64)        
    print bv1           
    FILEOUT = open( 'junk4.txt', 'w' )
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

