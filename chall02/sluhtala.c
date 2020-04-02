#include <stdlib.h>

static	char base_16(int n)
{
	char c;

	if (n < 10)
		return (n + '0');
	else
		return (n - 10 + 'a');
}

char *hv_rgb2hex(int r, int g, int b)
{
	char *hex;
	
	if (r < 0 || g < 0 || b < 0 || r > 255 || g > 255 || b > 255)
		return (NULL);
	if (!(hex = (char*)malloc(sizeof(char) * 7 + 1)))
		return (NULL);
	hex[7] = '\0';
	hex[0] = '#';
	hex[1] = base_16(r / 16);
	hex[2] = base_16(r % 16);
	hex[3] = base_16(g / 16);
	hex[4] = base_16(g % 16);
	hex[5] = base_16(b / 16);
	hex[6] = base_16(b % 16);
	return (hex);
}
