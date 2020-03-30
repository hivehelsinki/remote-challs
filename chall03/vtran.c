#include <string.h>
#include <stdlib.h>

static char*    light_itoa_base(int nb, int base)
{
    char str[17];
    char ret[3];

    strcpy(str, "0123456789abcdef");
    ret[2] = '\0';
    ret[1] = str[nb % base];
    ret[0] = str[(nb / base) % base];
    return (strdup(ret));
}

char* hv_rgb2hex(int r, int g, int b)
{
    char ret[8];

    if (r > 255 || g > 255 || b > 255 || r < 0 || g < 0 || b < 0)
        return (NULL);
    strcpy(ret, "#");
    strcat(ret, light_itoa_base(r, 16));
    strcat(ret, light_itoa_base(g, 16));
    strcat(ret, light_itoa_base(b, 16));
    return (strdup(ret));
}