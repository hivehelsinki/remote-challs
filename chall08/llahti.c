int		ft_cie(char *str, int i)
{
	if (i == 0)
		return 0;
	return (str[i - 1] == 'c');
}

int		ft_cei(char *str, int i)
{
	if (i == 0)
		return 0;
	return (str[i - 1] == 'c');
}

int		ft_ie_except_after_c(char *str)
{
	int i = 0;

	while (str[i] != '\0' && str[i + 1] != '\0')
	{
		if (str[i] == 'i' && str[i + 1] == 'e' && ft_cie(str, i))
			return 0;
		else if (str[i] == 'e' && str[i + 1] == 'i' && !ft_cei(str, i))
			return 0;
		i++;
	}
	return 1;
}
