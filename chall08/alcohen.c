#include <stdlib.h>

/*
**  Return 1 if "ei" after "c", 0 otherwise
*/
static int check_ei(char *str, size_t i)
{
    if (str[i + 1] && str[i + 1] == 'i')
    {
        if (i > 0 && str[i - 1] && str[i - 1] == 'c')
            return (1);
        else
            return (0);
    }
    return (1);
}

/*
**  Return 0 if "ie" after "c", 1 otherwise
*/
static int check_ie(char *str, size_t i)
{
    if (str[i + 1] && str[i + 1] == 'e')
        {
            if (i > 0 && str[i - 1] && str[i - 1] == 'c')
                return (0);
        }
    return (1);
}


int ft_ie_except_after_c(char* str)
{
    size_t  i;

    i = 0;
    while (str[i])
    {
        if (str[i] == 'e')
        {
            if (check_ei(str, i) == 0)
                return (0);
        }
        else if (str[i] == 'i')
            if (check_ie(str, i) == 0)
                return (0);
        i++;
    }
    return (1);
}