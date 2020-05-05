#include <string.h>
#include <stdbool.h>

static int	test_ei(char *str)
{
	char	*strcpy;

	strcpy = str;
	while ((strcpy = strstr(strcpy, "ei")))
	{
		if (strcpy - str > 0)
			if (str[strcpy - str - 1] != 'c')
				return (false);
		strcpy++;
	}
	return (true);
}

static int	test_ie(char *str)
{
	char	*strcpy;

	strcpy = str;
	while ((strcpy = strstr(strcpy, "ie")))
	{
		if (strcpy - str > 0)
			if (str[strcpy - str - 1] == 'c')
				return (false);
		strcpy++;
	}
	return (true);
}

int		ft_ie_except_after_c(char *str)
{
	if (!str)
		return (0);
	return (test_ei(str) && test_ie(str));
}
