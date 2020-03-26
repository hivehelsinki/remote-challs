#include <stdlib.h>
#include <string.h>

int	hv_necklace(char *s1, char *s2)
{
	char	swap;
	char	*temp;
	int	i;
	int	rotations;
	int	len;

	len = strlen(s2);
	if (strcmp(s1, s2) == 0)
		return (1);
	if (strlen(s1) != strlen(s2))
		return (0);
	temp = (char *)malloc(sizeof(char) * len + 1);
	strcpy(temp, s2);
	rotations = 0;
	while (rotations < len)
	{
		i = -1;
		swap = temp[0];
		while (++i < len - 1)
			temp[i] = temp[i + 1];
		temp[len - 1] = swap;
		if (strcmp(s1, temp) == 0)
			return (1);
		rotations++;
	}
	return (0);
}
