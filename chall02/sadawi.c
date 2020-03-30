
#include <stdio.h>
#include <stdlib.h>

char	*hv_rgb2hex(int r, int g, int b)
{
	char *str = malloc(8);
	sprintf(str, "#%02x%02x%02x\n", (r), (g), b);
	return (str);
}