#include <stdlib.h>

static void		int2hex(int color, char *str)
{
	int		i1;
	int		i2;
	int		color2;

	i1 = 0;
	i2 = 1;
	while (str[i1])
		i1++;
	while (i2 >= 0)
	{
		color2 = color % 16;
		if (color2 < 10)
			str[i1 + i2] = color2 + '0';
		else
			str[i1 + i2] = color2 - 10 + 'a';
		color = color / 16;
		i2--;
	}
}

char			*hv_rgb2hex(int r, int g, int b)
{
	char		*hex;

	if (r < 0 || g < 0 || b < 0 || r > 255 || g > 255 || b > 255)
		return (0);
	if (!(hex = (char*)malloc(sizeof(char) * 8)))
		return (0);
	hex[0] = '#';
	hex[7] = '\0';
	int2hex(r, hex);
	int2hex(g, hex);
	int2hex(b, hex);
	return (hex);
}
