/* 
** hv_rgb2hex - A function to convert colours in RGB
** to Hexadecimal value
*/
#include <stdio.h>
#include <stdlib.h>

/*
** Validate if rgb values are between 0 and 255
*/
int validate_rgb(r, g, b)
{
    if (r < g && r < b && r < 0)
        return (0);
    if (r < g && b < r && b < 0)
        return (0);   
    if (r > g && g < b && g < 0)
        return (0);  
    if (r > g && r > b && r > 255)
        return (0);
    if (r > g && b > r && b > 255)
        return (0);   
    if (r < g && g > b && g > 255)
        return (0); 
    return (1);
}

char *hv_rgb2hex(int r, int g, int b)
{
    if (validate_rgb(r, g, b))
    {
        char *hex;
        hex = (char*)malloc(7 * sizeof(char) + 1);
        sprintf(hex, "#%02x%02x%02x", r, g, b);
        return (hex);       
    }
    return NULL; 
}