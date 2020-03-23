
#include <string.h>

char	*move_to_end(char *str, size_t len)
{
	char	temp;
	char	*res;
	size_t	i;

	i = 0;
	temp = str[0];
	res = strdup(str);
	while (i < len - 1)
	{
		res[i] = str[i + 1];
		i++;
	}
	res[i] = temp;
	return (res);
}

int		hv_necklace(char *str1, char *str2)
{
	size_t	len;
	size_t	i;

	len = strlen(str1);
	if (len != strlen(str2))
		return (0);
	if (len == 0)
		return (1);
	i = 0;
	while (i < len)
	{
		if (strcmp(str1, str2) == 0)
			return (1);
		str1 = move_to_end(str1, len);
		i++;
	}
	return (0);
}
