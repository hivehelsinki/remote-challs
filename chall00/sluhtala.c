int	ft_strlen(char *str)
{
	int i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

int	ft_strcmp_offset(char *s1, char *s2, int os)
{
	int i;
	int len;

	len = ft_strlen(s1);
	i = 0;
	while ((s1[i] || s2[i]))
	{
		
		if (s1[i] != s2[i + os])
			return (s1[i] - s2[i + os]);
		i++;
		if (i + os >= len)
		{
			if(os <= 0)
				break ;
			os = -i;
		}
	}
	return (0);
}

int	hv_necklace(char *s1, char *s2)
{
	int len;
	int i;

	i = 0;
	len = ft_strlen(s1);
	if (len != ft_strlen(s2))	
		return (0); 
	while (i < len)
	{
		if (ft_strcmp_offset(s1, s2, i) == 0)
			return (1);
		i++;
	}
	if (len == 0)
		return (1);
	return (0);
}
