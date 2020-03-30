#include <stdio.h>
#include <stdlib.h>

int		ft_int_clamp(int nb, int min, int max)
{
	if (nb < min)
		return (min);
	if (nb > max)
		return (max);
	return (nb);
}

char *hv_rgb2hex(int r, int g, int b)
{
	int				rgb[3];
	unsigned int 	color;
	char			*color_string;

	if (!(color_string = (char *)malloc(sizeof(char) * 8)))
		return NULL;

	rgb[0] = ft_int_clamp(r, 0, 255);
	rgb[1] = ft_int_clamp(g, 0, 255);
	rgb[2] = ft_int_clamp(b, 0, 255);
	color = rgb[0] << 16 | rgb[1] << 8 | rgb[2];
	sprintf(&color_string[1], "%x", color);
	color_string[0] = '#';
	return(color_string);
}
