#include <string.h>
#include <stdbool.h>

static int	test(char *str, char *test, bool must_follow_c)
{
	char	*strcpy;

	strcpy = str;
	while ((strcpy = strstr(strcpy, test)))
	{
		if (strcpy - str > 0)
			if (must_follow_c ? str[strcpy - str - 1] != 'c' :
				str[strcpy - str - 1] == 'c')
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
	return (test(str, "ei", true) && test(str, "ie", false));
}
