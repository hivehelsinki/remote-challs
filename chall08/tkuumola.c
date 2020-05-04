#include <string.h>

int match(char *str, char *needle)
{
    int flag = 0;

    while( (str=strstr(str, needle)) != NULL)
    {
        flag = 1;
        str++;
    }
    return (flag);
}

int ft_ie_except_after_c(char *str)
{    
    if (str == NULL || strlen(str) == 0)
        return(0);
    
    if (match(str, "ei") == 0 && match(str, "ie") == 0)
        return (1);

    int cei_word = match(str, "cei");
    int ei_word = match(str, "ei");
    int cie_word = match(str, "cie");
    int ie_word = match(str, "ie");

    if (cei_word == 1 && cie_word == 0) 
        return (1);
    if (ie_word == 1 && cie_word == 0 && ei_word == 0 && strlen(str) > 2)
        return (1);
    return (0);
}
