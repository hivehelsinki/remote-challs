#include <stdio.h>
#include <stdlib.h>

char	*hv_rgb2hex(int r, int g, int b)
{
	char *ret;

	if (r > 255 || r < 0 ||
		g > 255 || g < 0 ||
		b > 255 || b < 0)
		return (NULL);

	if (!(ret = (char *)malloc(sizeof(char) * 8)))
		return (NULL);

	sprintf(ret, "#%.2x%.2x%.2x", r, g, b);
	return (ret);
}
