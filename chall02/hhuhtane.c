#include <string.h>
#include <stdio.h>

size_t		hv_strlen(char str)
{
	size_t	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

size_t		hv_intlen_base(int n, int base)
{
	size_t		len;

	len = 1;
	if (n < 0)
		len++;
	while (n >= base || n <= -base)
	{
		n /= base;
		len++;
	}
	return (len);
}

char	*hv_itoa_base(int n, int base)
{
	size_t		n_len;
	size_t		temp;
	char		str;

	n_len = hv_intlen_base(n, base);
	if ((str = (char*)malloc(sizeof(char) * n_len)))
		return (NULL);
	str[n_len--] = '\0';
	while (n >= base || n <= -base)
	{
		temp = n % base;
		if (temp <= 9)
			str[n_len--] = temp + '0';
		else
			str[n_len--] = temp - 10 + 'a';
		n /= base;
	}
	if (temp <= 9)
		str[n_len] = temp + '0';
	else
		str[n_len] = temp - 10 + 'a';
	return (str);
}

char	*hv_strcat(char *s1, char *s2)
{
	size_t	i1;
	size_t	i2;

	i1 = hv_strlen(s1);
	i2 = 0;
	while (s2)
		s1[i1++] = s2[i2++];
	s1[i1] = '\0';
	return (s1);
}

char	*hv_rgb2hex(int r, int g, int b)
{
	char*	hex_str;
	char*	color_tmp;

	if (r < 0 | g < 0 | b < 0)
		return (0);
	if (r > 255 | g > 255 | b > 255)
		return (0);
	if ((hex_str = (char*)malloc(sizeof(char) * 8)))
		return (0);
	color_tmp = ft_itoa_base(r, 16);
	hv_strcat(hex_str, color_tmp)
	color_tmp = ft_itoa_base(g, 16);
	hv_strcat(hex_str, color_tmp)
	color_tmp = ft_itoa_base(b, 16);
	hv_strcat(hex_str, color_tmp)
	return (hex_str);
}

int		main(void)
{
	printf("%d\n", strcmp(hv_rgb2hex(252, 186, 3), "#fcba03"));

	return (0);
}
