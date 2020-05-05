#include <string.h>
#include <stdbool.h>

static int	test_case(char *str, char *test, bool follows_c)
{
	char	*s = str;
	while ((s = strstr(s, test)))
	{
		if (s - str > 0)
			if (follows_c ? str[s - str - 1] != 'c' : str[s - str - 1] == 'c')
				return (false);
		s++;
	}
	return (true);
}

int		ft_ie_except_after_c(char *str)
{
	if (!str)
		return (true);
	if (strcmp("ei", str) == 0)
		return (false);
	return (test_case(str, "ei", true) && test_case(str, "ie", false));
}
