#include <stdlib.h>

static char    *color_to_hex(int color)
{
    char *base16 = "0123456789abcdef";
    char *s;
    int idx;

    if (!(s = (char *)malloc(sizeof(char) * 8)))
        return (NULL);  
    idx = 6;
    s[idx + 1] = '\0';
    while (idx > 0)
    {
        s[idx] = base16[color % 16];
        color /= 16;
        idx--;
    }
    s[0] = '#';
    return (s);
}

char    *hv_rgb2hex(int r, int g, int b)
{
    int color;

    if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255)
        return (NULL);
    color = (r * 256 * 256) + (g * 256) + b;
    return (color_to_hex(color));
}
