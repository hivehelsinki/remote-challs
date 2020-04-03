#include <stdlib.h>

#define NOT_COLOR_INT(x) (x < 0 || x > 255)

static char	*ft_hex(int value, int index, char *str)
{
	char *hex;
	hex = "0123456789abcdef";
	str[index + 1] = hex[value % 16];
	value = value / 16;
	str[index] = hex[value % 16];
	return (str);
}

char		*hv_rgb2hex(int r, int g, int b)
{
	char *ret;

	if (NOT_COLOR_INT(r) || NOT_COLOR_INT(g) || NOT_COLOR_INT(b))
		return (NULL);
	ret = (char *)malloc(8);
	ret[0] = '#';
	ret[7] = '\0';
	ret = ft_hex(r, 1, ret);
	ret = ft_hex(g, 3, ret);
	ret = ft_hex(b, 5, ret);
	return (ret);
}