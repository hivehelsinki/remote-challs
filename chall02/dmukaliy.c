#include <stdlib.h>

void    put_hex(int num, char **str, int i)
{
    char    *hex = "0123456789abcdef";
    char    *res = *str;

    res[i + 1] = hex[num % 16];
    num /= 16;
    res[i] = hex[num % 16];
}

char    *hv_rgb2hex(int r, int g, int b)
{
    char    *res;

    res = (char*)malloc(sizeof(char) * 8);
    if (!res || r < 0 || g < 0 || b < 0 || r > 255 || g > 255 || b > 255)
        return (NULL);
    res[0] = '#';
    put_hex(r, &res, 1);
    put_hex(g, &res, 3);
    put_hex(b, &res, 5);
    res[7] = '\0';
    return (res);
}

