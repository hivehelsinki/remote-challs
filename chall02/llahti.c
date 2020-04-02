#include <stdlib.h>

char    *int_to_hexa(int nb, char *str, int i)
{
    char    *base = "0123456789abcdef";
    int     len = 2;

	while (len)
	{
		len--;
		str[i + len] = base[nb % 16];
		nb /= 16;
	}
	return (str);
}

char     *hv_rgb2hex(int r, int g, int b)
{
    char    *str;

    if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255)
        return NULL;
    if (!(str = (char*)malloc(sizeof(char) * 8)))
        return NULL; 
    str[0] = '#';
    int_to_hexa(r, str, 1);
    int_to_hexa(g, str, 3);
    int_to_hexa(b, str, 5);
    str[7] = 0;
    return str;
}
