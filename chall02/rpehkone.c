#include <stdlib.h>
#include <stdio.h>

char	*hv_rgb2hex(int r, int g, int b)
{
	char *res;
	char hex[3];

	if (r < 0 || g < 0 || b < 0 || r > 255 || g > 255 || b > 255)
		return (NULL);
	res = (char*)malloc(sizeof(char) * 8);
	res[0] = '#';
	sprintf(&hex[0], "%02x", r);
	res[1] = hex[0];
	res[2] = hex[1];
	sprintf(&hex[0], "%02x", g);
	res[3] = hex[0];
	res[4] = hex[1];
	sprintf(&hex[0], "%02x", b);
	res[5] = hex[0];
	res[6] = hex[1];
	res[7] = '\0';
	return (res);
}
