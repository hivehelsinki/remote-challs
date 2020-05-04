#include <string.h>

int ft_ie_except_after_c(char *str)
{    
    if (str == NULL || strlen(str) == 0)
        return(0);
    if (strstr(str, "ei") != NULL)
        return (strstr(str, "cei") != NULL ? 1 : 0);
    if (strstr(str, "ie") != NULL)
        return (strstr(str, "cie") != NULL ? 0 : 1);
    return(1);
}
