#include <stdlib.h>

static int	ft_strlen(char *str)
{
	int ret;

	ret = 0;
	while (*str)
	{
		str++;
		ret++;
	}
	return (ret);
}

static char	*ft_strcpy(char *str)
{
	char *ret;
	int i;

	i = 0;
	if (!(ret = (char *)malloc(ft_strlen(str) + 1)))
		return (NULL);
	while (str[i] != '\0')
	{
		ret[i] = str[i];
		i++;
	}
	ret[i] = '\0';
	return (ret);
}

static char	*swap_char(char *str)
{
	int i;
	char *tmp;

	tmp = ft_strcpy(str);
	i = 0;
	while (i < ft_strlen(tmp) - 1)
	{
		str[i] = tmp[i + 1];
		i++;
	}
	str[i] = tmp[0];
	free(tmp);
	return (str);
}

static int	ft_strequ(char *s1, char *s2)
{
	while (*s1)
	{
		if (*s1 == *s2)
		{
			s1++;
			s2++;
		}
		else
			return (0);
	}
	return (1);
}

int	hv_necklace(char *s1, char *s2)
{
	int	i;
	int	len;

	if (ft_strlen(s1) != ft_strlen(s2))
		return (0);
	if (ft_strlen(s1) == 1)
	{
		if (*s1 == *s2)
			return (1);
		else
			return (0);
	}
	i = 0;
	len = ft_strlen(s1);
	while (i < len)
	{
		if (ft_strequ(s1, s2) == 1)
			return (1);
		s2 = swap_char(s2);
		i++;
	}
	return (0);
}

