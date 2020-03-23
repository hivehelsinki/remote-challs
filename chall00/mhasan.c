#include <stdio.h>
#include <unistd.h>
#include <string.h>

int ft_strcmp(char *s1, char *s2)
{
	int i;

	i = 0;
	while (s1[i] == s2[i] && s1[i] != '\0' && s2[i] != '\0')
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

int hv_necklace(char *s1, char *s2)
{
	int s1_len;
	int s2_len;
	int i;
	int j;
	int k;
	int temp;
	char str_cpy[4096];

	s1_len = 0;
	while (s1[s1_len] != '\0')
		s1_len++;
	s2_len = 0;
	while (s2[s2_len] != '\0')
		s2_len++;
	if (s1_len == s2_len)
	{
		if (strcmp(s1, s2) == 0)
			return (1);
		i = 0;
		while (i < s1_len - 1)
		{
			j = 0;
			temp = i;
			while (temp < s1_len - 1)
			{
				str_cpy[j] = s1[temp + 1];
				j++;
				temp++;
			}
			k = 0;
			while (k <= i)
			{
				str_cpy[j] = s1[k];
				k++;
				j++;
			}
			str_cpy[j] = '\0';
			if (ft_strcmp(str_cpy, s2) == 0)
				return (1);
			i++;
		}
	}
	return (0);
}

