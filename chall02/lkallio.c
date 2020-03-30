#include <stdlib.h>

char	*hv_rgb2hex(int r, int g, int b)
{
	char	*out;
	int		i;

	b |= g * 0x100 | r * 0x10000;
	i = 7;
	if (!(out = (char *)malloc(8)))
		return (0);
	while (--i)
	{
		out[i] = b % 0x10 + (b % 0x10 > 9 ? 'a' - 10 : '0');
		b /= 0x10;
	}
	out[0] = '#';
	out[7] = 0;
	return (out);
}