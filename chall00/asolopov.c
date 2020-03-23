int	get_len(char *str)
{
	int cnt;

	cnt = 0;
	while (str[cnt] != '\0')
		cnt += 1;
	return (cnt);
}

int	ft_strequ(char const *s1, char const *s2)
{
	if (!s1 || !s2)
		return (0);
	if (get_len(s1) != get_len(s2))
		return (0);
	while (*s1 && *s2)
	{
		if (*s1 != *s2)
			return (0);
		s1++;
		s2++;
	}
	return (1);
}

int hv_necklace(char *s1, char *s2)
{
	int len;
	int x;
	int y;
	int z;
	int d;
	char *temp;

	if (!s1 || !s2)
		return (0);
	len = get_len(s1);
	d = 0;
	while (d < len) // d as counter to loop thorugh the string
	{
		y = 0;
		z = 0;
		x = d;
		temp = malloc(sizeof(char) * len + 1); // creating a temp to compare s2 to it later
		while (x < len) // adding main part to temp
		{
			temp[z] = s1[x];
			x += 1;
			z += 1;
		}
		while (y < d) // adding front part to the back of the temp
		{
			temp[z] = s1[y];
			y += 1;
			z += 1;
		}
		temp[z] = '\0';
		if (ft_strequ(temp, s2)) // comparing
			return (1);
		free(temp);
		d += 1;
	}
	return (0);
}
