#include <stdlib.h>

static void			flip(char *str, int start)
{
	char	tmp;

	tmp = str[start];
	str[start] = str[start + 1];
	str[start + 1] = tmp;
}

static char			*ft_itoa_hex(unsigned char nb, char *res, int j)
{
	int		i;
	char	*bases;

	bases = "0123456789abcdef";
	i = 0;
	while (nb != 0)
	{
		res[j] = bases[nb % 16];
		nb = nb / 16;
		i++;
		j++;
	}
	while (i < 2)
		res[j + i++] = '0';
	flip(res, j);
	return (res);
}

char				*hv_rgb2hex(int r_int, int g_int, int b_int)
{
	char				*rgb[3];
	char				*res;

	if (!(res = malloc(8)))
		return (NULL);
	res[0] = '#';
	res = ft_itoa_hex(r_int, res, 1);
	res = ft_itoa_hex(g_int, res, 3);
	res = ft_itoa_hex(b_int, res, 5);
	res[7] = '\0';
	return (res);
}
