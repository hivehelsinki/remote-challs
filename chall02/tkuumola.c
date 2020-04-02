#include <stdlib.h>
#include <stdio.h>

char *hv_rgb2hex(int r, int g, int b)
{
    char *str;
    char *temp;

    if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255)
        return (0);
    if(!(str = (char*)malloc(sizeof(char) * 8)))
        return (0);
    str[0] = '#';
    temp = &str[1];
    sprintf(temp, "%02x", r);
    temp = &str[3];
    sprintf(temp, "%02x", g);
    temp = &str[5];
    sprintf(temp, "%02x", b);
    str[7] = '\0'; 
    return (str);
}
