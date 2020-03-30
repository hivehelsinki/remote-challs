#include <stdlib.h>
#include <stdio.h>

char	*hv_rgb2hex(int r, int g, int b)
{
	char *res;
	char hex[5];

	res = (char*)malloc(sizeof(char) * 8);
	res[0] = '#';
	sprintf(&hex[0], "%04x", r);
	res[1] = hex[2];
	res[2] = hex[3];
	sprintf(&hex[0], "%04x", g);
	res[3] = hex[2];
	res[4] = hex[3];
	sprintf(&hex[0], "%04x", b);
	res[5] = hex[2];
	res[6] = hex[3];
	res[7] = '\0';
	return (res);
}
