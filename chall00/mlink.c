size_t ft_strlen(char *s)
{
    size_t	i;

	i = 0;
	while (s[i] != '\0')
		i++;
	return (i);
}

int hv_necklace(char *s1, char *s2)
{
    int len;
    int len2;
    int i;
    int j;
    int x;

    x = -1;
    len = ft_strlen(s1);
    len2 = ft_strlen(s2);
    if (!s1 || !s2 || (len != len2))
        return (0);
    if (len == 0 && len2 == 0)
        return (1);
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
