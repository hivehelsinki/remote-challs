/* 
** hv_rgb2hex - A function to convert colours in RGB
** to Hexadecimal value
*/
#include <stdio.h>
#include <stdlib.h>

char *hv_rgb2hex(int r, int g, int b)
{
    char *hex;

    hex = (char*)malloc(7 * sizeof(char) + 1);
    sprintf(hex, "#%02x%02x%02x", r, g, b);
    return (hex);
}