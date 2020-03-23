int		ft_strequ(char *st1, char *st2)
{
	while (*st1 && *st2 && *st1 == *st2)
	{
		st1++;
		st2++;
	}
	if (*st1 != *st2)
		return (0);
	return (1);
}

void	ft_rotate(char *str)
{
	int		i;
	char	tmp;

	i = 0;
	tmp = str[0];
	while (str[i + 1])
	{
		str[i] = str[i + 1];
		i++;
	}
	str[i] = tmp;
}

int		hv_necklace(char *s1, char *s2)
{
	int		i = 0;
	int		len = 0;

	if (!s1 || !s2)
		return (0);
	while (s1[len])
		len++;
	while (i++ < len && !ft_strequ(s1, s2))
		ft_rotate(s2);
	if (ft_strequ(s1, s2))
		return (1);
	return (0);
}
