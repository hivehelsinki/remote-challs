int	ft_ie_except_after_c(char *str)
{
	for (int i = 0; str[i]; i++)
	{
		if (str[i] == 'e' && str[i + 1] && str[i + 1] == 'i')
		{
			if (i && str[i - 1] != 'c')
				return (0);
		}
		else if (str[i] == 'i' && str[i + 1] && str[i + 1] == 'e')
			if (i && str[i - 1] == 'c')
				return (0);
	}
	return (1);
}
