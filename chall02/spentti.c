#include <stdlib.h>

char	*ft_itoa_hex(unsigned long long n, char *str, int i)
{
	if (n < 16)
	{
		str[i - 1] = '0';
		if (n == 0)
			str[i] = '0';
	}
	while (n > 0)
	{
		str[i] = (n % 16 < 10) ? '0' + n % 16 : n % 16 + 'a' - 10;
		n = n / 16;
		i--;
	}
	return (str);
}

char *hv_rgb2hex(int r, int g, int b)
{
	char *str;

	if (!(str = (char *)malloc(sizeof(char) * 8)))
		return (NULL);
	str[0] = '#';
	str = ft_itoa_hex(r, str, 2);
	str = ft_itoa_hex(g, str, 4);
	str = ft_itoa_hex(b, str, 6);
	str[7] = '\0';
	return (str);
}
