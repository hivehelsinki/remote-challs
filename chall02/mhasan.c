#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *hv_rgb2hex(int r, int g, int b)
{
    char s1[3];
    char *str;

    if (r < 0 || g < 0 || b < 0 || r > 255 || g > 255 || b > 255)
        return (0);
    if (!(str = (char *)malloc(sizeof(char) * 8)))
        return (NULL);
    strcpy(str, "#");
    sprintf(s1, "%02x", r);
    strcat(str, s1);
    sprintf(s1, "%02x", g);
    strcat(str, s1);
    sprintf(s1, "%02x", b);
    strcat(str, s1);
    return (str);
}