#include <stdio.h>

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

	len = get_len(s1);
	d = 0;
	temp = malloc(sizeof(char) * len + 1);
	while (d < len)
	{
		y = 0;
		z = 0;
		x = d;
		while (x < len)
		{
			temp[z] = s1[x];
			x += 1;
			z += 1;
		}
		while (y < d)
		{
			temp[z] = s1[y];
			y += 1;
			z += 1;
		}
		temp[z] = '\0';
		if (ft_strequ(temp, s2))
			return (1);
		d += 1;
	}
	return (0);
}
