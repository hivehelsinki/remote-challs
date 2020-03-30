#include <stdio.h>
#include <stdlib.h>

char	*hv_rgb2hex(int r, int g, int b)
{
	char *str;
	if (!(str = (char *)malloc(sizeof(char) * 8)))
		return (NULL);
	str[0] = '#';
	sprintf(&str[1], "%x", (r & 0xFF) << 16 | (g & 0xFF) << 8 | (b & 0xFF));
	str[7] == '\0';
	return (str);
}
