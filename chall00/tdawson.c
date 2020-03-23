#include <string.h>
#include <stdlib.h>

int hv_necklace(char *s1, char *s2)
{
	char *s1s1;

	if (!s1 || !s2 || strlen(s1) != strlen(s2))
		return (0);
	if (!(s1s1 = malloc(strlen(s1) * 2 + 1)))
		return (0);
	strcpy(s1s1, s1);
	strcat(s1s1, s1);
	int ret = strstr(s1s1, s2) != NULL;
	free(s1s1);
	return ret;
}
