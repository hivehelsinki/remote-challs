int     is_match(char *s1, char *s2, int i, int j)
{
    int start = i;

    while (s1[i] != 0)
    {
        if (s1[i] != s2[j])
            return 0;
        i++;
        j++;
    }
    i = 0;
    while (i < start)
    {
        if (s1[i] != s2[j])
            return 0;
        i++;
        j++;  
    }
    return (s2[j] == 0);
}

int     hv_necklace(char *s1, char *s2)
{
    int     i;
    int     j;

    if (!s1 && !s2)
        return 1;
    if (!s1 || !s2)
        return 0;

    i = 0;
    j = 0;
    if (s1[i] == 0 && s2[j] == 0)
        return 1;
    while (s1[i] != 0)
    {
        if (s1[i] == s2[j] && is_match(s1, s2, i, j))
            return 1;
        i++;
    }
    return 0;
}