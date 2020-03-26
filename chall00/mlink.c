int ft_strlen(char *s)
{
    int	i;

	i = 0;
	while (s[i] != '\0')
		i++;
	return (i);
}

int hv_necklace(char *s1, char *s2)
{
    int len;
    int i;
    int j;
    int x;

    x = -1;
    if (!s1 || !s2 || (ft_strlen(s1) != ft_strlen(s2)))
        return (0);
    if (ft_strlen(s1) == 0 && ft_strlen(s2) == 0)
        return (1);
    len = ft_strlen(s1);
    while (len > ++x)
    {
        j = 0;
        i = x;
        if (s1[i] == s2[j])
        {
            while (s1[i] && s1[i] == s2[j++])
                i++;
            if (s1[i] != '\0')
                break;
            i = 0;
            while (s2[j] && s1[i] == s2[j++])
                i++;
            if (s2[j] == '\0')
                return (1);
        }
    }
    return (0);
}
