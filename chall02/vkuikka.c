#include <string.h>

static void		ft_hex_to_str(char *str, int num)
{
	char *hex;
	
	hex = "0123456789abcdef";
	str[1] = hex[num % 16];
	str[0] = hex[num / 16 % 16];
}

char			*hv_rgb2hex(int r, int g, int b)
{
	char	*res;

	if (r < 0 || r > 255 ||
		g < 0 || g > 255 ||
		b < 0 || b > 255)
		return (NULL);
	if (!(res = strdup("#000000")))
		return (NULL);
	ft_hex_to_str(res + 1, r);
	ft_hex_to_str(res + 3, g);
	ft_hex_to_str(res + 5, b);
	return (res);
}
