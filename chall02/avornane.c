#include <stdlib.h>

char		*hv_rgb2hex(int r, int g, int b)
{
	char	*rs;
	int		i;
	int		j;
	int		ar[3];

	j = 2;
	ar[0] = r;
	ar[1] = g;
	ar[2] = b;
	rs = (char*)malloc(sizeof(char) * 7);
	rs[7] = '\0';
	rs[0] = '#';
	i = 7;
	while (i-- > 1)
	{
		rs[i] = (ar[j] % 16 < 10) ? ar[j] % 16 + '0' : ar[j] % 16 + 'a' - 10;
		ar[j] /= 16;
		if (ar[j] <= 1)
		{
			(i % 2 == 0) ? rs[--i] = '0' : 0;
			j--;
		}
	}
	return (rs);
}
