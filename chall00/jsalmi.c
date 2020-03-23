#include <string.h>

int hv_necklace(char *s1, char *s2)
{
	int fi = 0;
	int si = 0;
	int start = 0;
	if (strlen(s1) != strlen(s2))
		return (0);
	if (!s1[0] && !s2[0])
		return (1);
	while (s2[start])
	{
		si = start;
		fi = 0;
		while (s1[fi] == s2[si])
		{
			si++;
			fi++;
			if (!s2[si])
				si = 0;
			if (!s1[fi])
				return (1);
		}
		start++;
	}
	return (0);
}
