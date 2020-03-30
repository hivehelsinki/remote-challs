#include <stdlib.h>

char *hv_rgb2hex(int r, int g, int b)
{
    char *str;
    char *hex;

    hex = "0123456789abcdef";
    if (r < 0 || g < 0 || b < 0 || r > 255 || g > 255 || b > 255)
        return (NULL);
    str = (char*)malloc(sizeof(char) * 8);
    str[7] = '\0';
    str[0] = '#';
    if (r > 16){
        str[1] = hex[r % 16];
        r /= 16;
    }
    else
        str[1] = '0';
    str[2] = hex[r % 16];
    if (g > 16){
        str[3] = hex[g % 16];
        g /= 16;
    }
    else
        str[3] = '0';
    str[4] = hex[g % 16];
    if (b > 16){
        str[5] = hex[b % 16];
        b /= 16;
    }
    else
        str[5] = '0';
    str[6] = hex[b % 16];
    return (str);
}
