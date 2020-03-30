#include <stdio.h>
#include <stdlib.h>

char *hv_rgb2hex(int r, int g, int b)
{
	char *hex_str;

	if (!(hex_str = malloc(8)))
		return NULL;
	unsigned int hex = ((r & 0xff) << 16) + ((g & 0xff) << 8) + (b & 0xff);
	sprintf(hex_str, "#%06x", hex);
	return hex_str;
}
