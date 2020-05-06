int	ft_ie_except_after_c(char *str)
{
	if (*str == 'e' && *(str + 1) == 'i')
		return (0);
	while (*(str++))
	{
		if (*str == 'i' &&
			*(str + 1) == 'e' &&
			*(str - 1) == 'c')
			return (0);
		else if (*str == 'e' &&
			*(str + 1) == 'i' &&
			*(str - 1) != 'c')
			return (0);
	}
	return (1);
}
