#include <stdlib.h>

static void			ft_strrev(char *str)
{
	int		i;
	char	tmp;

	i = 0;
	while (i < 1)
	{
		tmp = str[i];
		str[i] = str[2 - i - 1];
		str[2 - i - 1] = tmp;
		i++;
	}
}

static char			*ft_itoa_hex(unsigned char nb)
{
	int		i;
	char	*arr;
	char	*bases;

	bases = "0123456789abcdef";
	if (!(arr = malloc(2 + 1)))
		return (NULL);
	i = 0;
	while (nb != 0)
	{
		arr[i++] = bases[nb % 16];
		nb = nb / 16;
	}
	while (i < 2)
		arr[i++] = '0';
	ft_strrev(arr);
	arr[2] = '\0';
	return (arr);
}

static void			copy_rgb_part_str(int start, int end, char *dst, char *src)
{
	int		i;
	int		j;

	i = start;
	j = 0;
	while (i < end)
		dst[i++] = src[j++];
}

char				*hv_rgb2hex(int r_int, int g_int, int b_int)
{
	char				*rgb[3];
	char				*res;

	if (!(rgb[0] = ft_itoa_hex(r_int)) ||
		!(rgb[1] = ft_itoa_hex(g_int)) ||
		!(rgb[2] = ft_itoa_hex(b_int)) ||
		!(res = malloc(8)))
		return (NULL);
	res[0] = '#';
	copy_rgb_part_str(1, 3, res, rgb[0]);
	copy_rgb_part_str(3, 5, res, rgb[1]);
	copy_rgb_part_str(5, 7, res, rgb[2]);
	res[8] = '\0';
	free(&rgb[0]);
	free(&rgb[1]);
	free(&rgb[2]);
	return (res);
}
