#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char	*rotone(char *s1)
{
	int len;
	int i;
	char x;
	char *str;
  
	len = strlen(s1);
	str = (char *)malloc(sizeof(char) * (len + 1));
	str[len] = 0;
	x = s1[len - 1];
	i = len - 1;
	while(i > 0)
	{
		str[i] = s1[i - 1];
		i--;
	}
	str[0] = x;
	return (str);
}

int hv_necklace(char *s1, char *s2)
{
	int i;
	int len;
	char *tmp;
	char *tmp2;

	if (!s1[0] && !s2[0])
		return (1);
	len = strlen(s1);
	i = 0;
	tmp = rotone(s1);
	while(i < len)
	{
		if (strcmp(tmp, s2) == 0)
		{
			free(tmp);
			return (1);
		}
		tmp2 = tmp;
		tmp = rotone(tmp);
		free(tmp2);
		i++;
	}
	return (0);
}