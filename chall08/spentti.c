int ft_ie_except_after_c(char *str)
{
	int i;

	i = 0;
	while (str[i + 1] != '\0')
	{
		if (str[i] == 'c' && str[i + 1] == 'i' && str[i + 2] == 'e')
			return (0);
		if ((i == 0 || str[i - 1] != 'c') && str[i] == 'e' && str[i + 1] == 'i')
			return (0);
		i++;
	}
	return (1);
}
