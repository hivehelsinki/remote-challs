#include <stdio.h>
#include <stdlib.h>

int	check(int value)
{
	return ((value < 0 || value > 255) ? 0 : 1);
}

char	*hv_rgb2hex(int r, int g, int b)
{
	char *str;
	if (check(r) == 0 || check(g) == 0 || check(b) == 0)
		return (NULL);
	if (!(str = (char *)malloc(sizeof(char) * 8)))
		return (NULL);
	sprintf(&str[0], "#%x", (r & 0xFF) << 16 | (g & 0xFF) << 8 | (b & 0xFF));
	str[7] == '\0';
	return (str);
}
