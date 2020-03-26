#include <stdlib.h>
#include <string.h>

int		compare_len(const char *s1, const char *s2)
{
	int s1_len;
	int s2_len;

	s1_len = 0;
	s2_len = 0;
	while (*s1++)
		s1_len++;
	while (*s2++)
		s2_len++;
	if (s1_len != s2_len)
		return (-1);
	return (s1_len);
}

char	*rotate_necklace(const char *s2, int neck_len)
{
	char *rotated;
	char first;

	if (!(rotated = (char *)malloc(sizeof(char) * (neck_len + 1))))
		exit(1);
	rotated[neck_len] = '\0';
	first = s2[neck_len - 1];
	while (neck_len-- > 1)
		rotated[neck_len] = s2[neck_len - 1];
	rotated[0] = first;
	return (rotated);
}

int		hv_necklace(char *s1, char *s2)
{
	int neck_len;
	int rounds_to_try;
	char *rotated_necklace;
	char *old_necklace;

	neck_len = compare_len(s1, s2);
	if (neck_len < 0)
		return (0);
	rounds_to_try = neck_len;
	if (strcmp(s1, s2) == 0)
		return (1);
	else
	{
		rotated_necklace = rotate_necklace(s2, neck_len);
		while (rounds_to_try--)
		{
			if (strcmp(s1, rotated_necklace) == 0)
			{
				free(rotated_necklace);
				return (1);
			}
			old_necklace = rotated_necklace;
			rotated_necklace = rotate_necklace(rotated_necklace, neck_len);
			free(old_necklace);
		}
	}
	return (0);
}
