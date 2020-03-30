#include <stdlib.h>
#include <string.h>

int		ft_strequ(char *st1, char *st2)
{
	while (*st1 && *st2 && *st1 == *st2)
	{
		st1++;
		st2++;
	}
	if (*st1 != *st2)
		return (0);
	return (1);
}

void	ft_rotate(char *str)
{
	size_t		i;
	char		tmp;

	i = 0;
	tmp = str[0];
	while (str[i + 1])
	{
		str[i] = str[i + 1];
		i++;
	}
	str[i] = tmp;
}

int		hv_necklace(char *s1, char *s2)
{
	size_t		i;
	size_t		len;
	char 		*str1;
	char		*str2;

	i = 0;
	if (!s1 || !s2 || strlen(s1) != strlen(s2))
		return (0);
	len = strlen(s1);
	if (!(str1 = (char*)malloc(sizeof(char) * len)))
		return (0);
	if (!(str2 = (char*)malloc(sizeof(char) * len)))
		return (0);
	strcpy(str1, s1);
	strcpy(str2, s2);
	while (i++ < len && !ft_strequ(str1, str2))
		ft_rotate(str2);
	if (ft_strequ(str1, str2))
		return (1);
	free(str1);
	free(str2);
	return (0);
}
