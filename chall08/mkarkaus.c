int		ft_ie_except_after_c(char *str)
{
	int		i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] == 'e' && str[i + 1] == 'i' && str[i - 1] != 'c')
			return (0);
		if (str[i] == 'i' && str[i + 1] == 'e' && str[i - 1] == 'c')
			return (0);
		i++;
	}
	return (1);
}
