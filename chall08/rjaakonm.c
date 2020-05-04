int ft_ie_except_after_c(char *str)
{
	int i = 0;
	int ok = 1;

	while (str[i])
	{
		if (str[i] == 'i' && str[i + 1] == 'e')
			if (i > 0 && str[i - 1] == 'c')
				return (0);
		if (str[i] == 'e' && str[i + 1] == 'i')
			if (i == 0 || str[i - 1] != 'c')
				return (0);
		i++;
	}
	return (1);
}
