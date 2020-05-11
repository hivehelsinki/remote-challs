int ft_ie_except_after_c(char *str)
{
    int i;
    int len;
    int exc;
    
    i = 0;
    len = 0;
    exc = 1;
    while (str[i++] != '\0')
        len++;
    i = 0;
    while (str[i] != '\0')
    {
        if (str[i] == 'e' && (len - (i + 1)) >= 1)
        {
            if (i != 0)
            {
                if (str[i - 1] == 'c' && str[i + 1] == 'i')
                    return (1);
            }
            if (str[i + 1] == 'i')
                exc = 0;
        }
        else if (str[i] == 'i' && (len - (i + 1)) >= 1)
        {
            if (i != 0)
            {
                if (str[i - 1] != 'c' && str[i + 1] == 'e')
                    return (1);
            }
            else if (i == 0 && str[i + 1] == 'e')
                return (1);
            if (str[i + 1] == 'e')
                exc = 0;
        }
        i++;
    }
    return (exc);
}
