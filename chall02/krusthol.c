#include <stdlib.h>

static void	convert_hex(char *hex_table, char *hex_value, int value, int loc)
{
	if (value > 15)
	{
		hex_value[loc + 1] = hex_table[value % 16];
		hex_value[loc] = hex_table[(value /= 16)];
	}
	else
	{
		hex_value[loc] = '0';
		hex_value[loc + 1] = hex_table[value];
	}
}

static char	*error_range(char *hex_value)
{
	hex_value[1] = 'e';
	hex_value[2] = 'r';
	hex_value[3] = 'r';
	hex_value[4] = 'o';
	hex_value[5] = 'r';
	hex_value[6] = '!';
	return (hex_value);
}

char		*hv_rgb2hex(int r, int g, int b)
{
	char	hex_table[16] = { "0123456789abcdef" };
	char	*hex_value;

	if (!(hex_value = (char *)malloc(sizeof(char) * 8)))
		return (NULL);
	hex_value[0] = '#';
	hex_value[7] = '\0';
	if ((r > 255 || g > 255 || b > 255) || (r < 0 || g < 0 || b < 0))
		return (error_range(hex_value));
	convert_hex(hex_table, hex_value, r, 1);
	convert_hex(hex_table, hex_value, g, 3);
	convert_hex(hex_table, hex_value, b, 5);
	return (hex_value);
}
