int ft_ie_except_after_c(char *str)
{
	for (int i = 0; str[i]; i++)
	{
		if (str[i] == 'c' && str[i + 1] == 'i' && str[i + 2] == 'e')
				return (0);
		if (str[i] == 'e' && str[i + 1] == 'i' && (i == 0 || str[i - 1] != 'c'))
				return (0);
	}
	return (1);
}
