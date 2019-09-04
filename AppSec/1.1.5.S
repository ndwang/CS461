.global _main
.section .text

_main:

push	%ebp
mov	%esp,%ebp

mov	$11,%eax
push	$0x0068732f
push	$0x6e69622f
mov	%esp,%ebx
xor	%ecx,%ecx
xor	%edx,%edx
int	$0x80
leave
ret
