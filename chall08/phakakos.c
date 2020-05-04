long	ft_strlen(char *str)
{
	long	i;
	
	i = 0;
	while (str[i])
		i++;
	return (i)
}

int		following(char *str, char c)
{
	if (str[0] == 'c' && str[2] == c)
		return (1);
	return (0);
}

int		ft_ie_except_after_c(char *str)
{
	int		rtn;
	long	i;
	
	i = ft_strlen(str) - 1;
	rtn = 1;
	while (rtn == 1 && --i >= 0)
	{
		if (str[i] == 'e')
		{
			if (i == 0 && str[i + 1] == 'i')
				return (0);
			rtn = following(&str[i - 1], 'i');
		}
		else if (str[i] == 'i' && i > 0)
			rtn = !(following(&str[i - 1], 'e'));
	}
	return (rtn)
}