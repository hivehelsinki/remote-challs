static int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

static int cmp(char *s1, char *s2, int len, int pos2)
{
	int pos1;
	int	i;

	pos1 = 0;
	i = 0;
	while (i < len) {
		if (s1[pos1] != s2[pos2])
			return (0);
		pos1++;
		pos2++;
		if (pos1 >= len)
			pos1 = 0;
		if (pos2 >= len)
			pos2 = 0;
		i++;
	}
	return (1);
}

int hv_necklace(char *s1, char *s2) {
	int		i;
	int		len;
	int		len2;

	i = 0;
	len = ft_strlen(s1);
	len2 = ft_strlen(s2);
	if (len != len2)
		return (0);
	if (len == len2 && len == 0)
		return (1);
	while (i < len)
	{
		if (cmp(s1, s2, len, i))
			return (1);
		i++;
	}
	return (0);
}

