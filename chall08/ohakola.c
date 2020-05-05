#include <string.h>
#include <stdbool.h>

static int	test(char *str, char *test, bool follows_c)
{
	char	*strcpy;

	strcpy = str;
	while ((strcpy = strstr(strcpy, test)))
	{
		if (strcpy - str > 0)
			if (follows_c ? str[strcpy - str - 1] == 'c' :
				str[strcpy - str - 1] != 'c')
				return (false);
		strcpy++;
	}
	return (true);
}

int		ft_ie_except_after_c(char *str)
{
	if (!str)
		return (true);
	if (strcmp("ei", str) == 0)
		return (false);
	return (test(str, "ei", false) && test(str, "ie", true));
}
