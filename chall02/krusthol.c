#include <stdlib.h>

void	double_hex_color(char *hex, char *rgb_hex_value, int value, int loc)
{
	rgb_hex_value[loc] = hex[value % 16];
	rgb_hex_value[loc + 1] = hex[(value /= 16) % 16];
}

void	single_hex_color(char *hex, char *rgb_hex_value, int value, int loc)
{
	rgb_hex_value[loc] = '0';
	rgb_hex_value[loc + 1] = hex[value];
}

char	*error_range(char *rgb_hex_value)
{
	rgb_hex_value[1] = 'e';
	rgb_hex_value[2] = 'r';
	rgb_hex_value[3] = 'r';
	rgb_hex_value[4] = 'o';
	rgb_hex_value[5] = 'r';
	rgb_hex_value[6] = '!';
	return (rgb_hex_value);
}

char	*hv_rgb2hex(int r, int g, int b)
{
	char hex[16] = { "0123456789abcdef" };
	char *rgb_hex_value;

	if (!(rgb_hex_value = (char *)malloc(sizeof(char) * 8)))
		return (NULL);
	rgb_hex_value[0] = '#';
	rgb_hex_value[7] = '\0';
	if ((r > 255 || g > 255 || b > 255)
		|| (r < 0 || g < 0 || b < 0))
		return (error_range(rgb_hex_value));
	if (r > 15)
		double_hex_color(hex, rgb_hex_value, r, 1);
	else
		single_hex_color(hex, rgb_hex_value, r, 1);
	if (g > 15)
		double_hex_color(hex, rgb_hex_value, g, 3);
	else
		single_hex_color(hex, rgb_hex_value, g, 3);
	if (b > 15)
		double_hex_color(hex, rgb_hex_value, b, 5);
	else
		single_hex_color(hex, rgb_hex_value, b, 5);
	return (rgb_hex_value);
}
