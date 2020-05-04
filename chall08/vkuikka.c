int	ft_ie_except_after_c(char *str)
{
	int		follows_rule;

	follows_rule = 1;
	if (*str == 'e' && *(str + 1) == 'i')
		return (0);
	while (*(str++))
	{
		if (*str == 'i' && *(str + 1) == 'e')
			follows_rule = (*(str - 1) != 'c');
		else if (*str == 'e' && *(str + 1) == 'i')
			follows_rule = (*(str - 1) == 'c');
		if (!follows_rule)
			return (0);
	}
	return (follows_rule);
}
