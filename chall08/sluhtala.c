int ft_ie_except_after_c(char *str)
{
	int i;

	i = 0;
	if (str == NULL)
		return (-1);
	if (str[0] == '\0')
		return (1);
	if (str[0] == 'e' && str[1] == 'i')
		return (0);
	while (str[i])
	{
		if (str[i] != 'c' && str[i + 1] == 'e' && str[i + 2] == 'i')
		{
			return (0);				
		}
		if (str[i] == 'c' && str[i + 1] == 'i' && str[i + 2] == 'e')
		{
			return (0);
		}
		i++;
	} 
	return (1);
}
