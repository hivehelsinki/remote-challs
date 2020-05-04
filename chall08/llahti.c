#include <string.h>

int		ft_ie(char *str, size_t i)
{
	if (i == 0)
		return 1;
	return (str[i - 1] != 'c');
}

int		ft_cei(char *str, size_t i)
{
	if (i == 0)
		return 0;
	return (str[i - 1] == 'c');
}

int		ft_ie_except_after_c(char *str)
{
	size_t i = 0;
	while (i < strlen(str) - 1)
	{
		if (str[i] == 'i' && str[i + 1] == 'e' && !ft_ie(str, i))
			return 0;
		else if (str[i] == 'e' && str[i + 1] == 'i' && !ft_cei(str, i))
			return 0;
		i++;
	}
	return 1;
}
