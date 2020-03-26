#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int hv_necklace(char *s1, char *s2)
{
	int	len;
	char	*s3;
	char	*s4;

	len = strlen(s1);
	if (strlen(s2) != len)
		return (0);
	if (!len && !strlen(s2))
		return (1);
	s3 = (char*)malloc(sizeof(char) * len);
	s4 = (char*)malloc(sizeof(char) * len);
	strcpy(s3, s1);
	strcpy(s4, s2);
	for (int i = 0; i < len; i++)
	{
		if (!strcmp(s3, s4))
			return (1);
		char c = s3[0];
		for (int j = 0; j < len - 1; j++)
			s3[j] = s3[j + 1];
		s3[len - 1] = c;
	}
	return (0);
}
