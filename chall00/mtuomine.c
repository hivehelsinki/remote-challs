#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static char *first_to_last(char *str)
{
	if (!str)
		return str;
	size_t len = strlen(str);
	if (len <= 1)
		return str;
	char *new = malloc(sizeof(char) * len + 1);
	const char first = str[0];
	memcpy(new, str + 1, len - 1);
	new[len - 1] = first;
	new[len] = '\0';
	return new;
}


int hv_necklace(char *s1, char *s2)
{
	if (!s1 || !s2)
		return (0);
	size_t a_len = strlen(s1);
	size_t b_len = strlen(s2);

	if (strcmp(s1, s2) == 0)
		return (1);
	if (a_len != b_len || a_len <= 1 || b_len <= 1)
		return (0);
	size_t i = a_len - 1;
	char *new = first_to_last(s1);
	char *temp;
	while (i > 0)
	{
		if (strcmp(new, s2) == 0)
		{
			free(new);
			return (1);
		}
		temp = new;
		new = first_to_last(temp);
		free(temp);
		i--;
	}
	free(new);
	return (0);
}
