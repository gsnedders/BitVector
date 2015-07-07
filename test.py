#!/usr/bin/env python


mylist = [[1,2], [3,4], [5,6]]

newlist = [x[0] for x in mylist]

newlist = reduce(list.__add__, mylist)

print(newlist)

"""

        return ''.join(map(lambda x: x.replace('0x', ''), map(hex, map(int, reduce(list.__add__, map(lambda x:x.divide_into_two(), [self[i:i+8] for i in range(0,self.size,8) ] ))))))


    def getTextFromBitVector(self):
        return ''.join(map(chr, map(int,[self[i:i+8] \
                             for i in range(0,self.size,8)])))
        '''
        text = []
        for i in range(0,self.size, 8) :
            char = self[i:i+8]
            text.append(chr(int(char)))
        text = ''.join(text)
        return text
        '''
    def getHexStringFromBitVector(self):
        return ''.join(map(lambda x: x.replace('0x', ''), map(hex, map(int, reduce(list.__add__, map(lambda x:x.divide_into_two(), [self[i:i+8] for i in range(0,self.size,8) ] ))))))
        '''
        hexText = []
        for i in range(0,self.size,8) :
            byte = self[i : i+8]
            [hex1, hex2] = byte.divide_into_two()
            hex1 = str(hex(int(hex1))).replace('0x', '').lower()
            hex2 = str(hex(int(hex2))).replace('0x', '').lower()
            hexByte = hex1 + hex2
            hexText.append(hexByte)
        hexText = ''.join(hexText) # More efficient.                           
        return hexText
        '''
"""


'''
adict = {'a':1, 'size':2}

print(adict)

if 'size' in adict: s = adict.pop('size')

if s >= 0:
    print("s is greater than 0")

print(s)
'''
