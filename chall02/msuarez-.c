/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   msuarez-.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: msuarez- <msuarez-@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 15:20:29 by msuarez-          #+#    #+#             */
/*   Updated: 2020/03/30 15:20:29 by msuarez-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <string.h>

static void		ft_bzero(void *s, size_t n)
{
	unsigned char	*p;
	size_t			i;

	p = (unsigned char*)s;
	i = 0;
	while (i < n)
	{
		p[i] = 0;
		i++;
	}
}

static void		*ft_memalloc(size_t size)
{
	void	*mem;

	if (!(mem = (void*)malloc(size)))
		return (NULL);
	ft_bzero(mem, size);
	return (mem);
}

static char		*ft_strnew(size_t size)
{
	char	*str;

	if (!(str = (char*)ft_memalloc(size + 1)))
		return (NULL);
	return (str);
}

static char		*ft_strdup(const char *s1)
{
	int		i;
	int		size;
	char	*new;

	size = 0;
	while (s1[size])
	{
		size++;
	}
	if (!(new = (char*)malloc(sizeof(char) * (size + 1))))
		return (NULL);
	i = 0;
	while (s1[i])
	{
		new[i] = s1[i];
		i++;
	}
	new[i] = '\0';
	return (new);
}

static char		*ft_strjoin(char const *s1, char const *s2)
{
	char	*new;

	if (!s1 && !s2)
		return (NULL);
	if (!s1)
		return (ft_strdup(s2));
	if (!s2)
		return (ft_strdup(s1));
	if (!(new = (char*)ft_strnew(strlen(s1) + strlen(s2))))
		return (NULL);
	strcpy(new, s1);
	strcat(new, s2);
	return (new);
}

static char		*check_value(int value)
{
	char	*tmp;

	tmp = ft_strnew(1);
	if (value == 10)
		tmp[0] = 'a';
	else if (value == 11)
		tmp[0] = 'b';
	else if (value == 12)
		tmp[0] = 'c';
	else if (value == 13)
		tmp[0] = 'd';
	else if (value == 14)
		tmp[0] = 'e';
	else if (value == 15)
		tmp[0] = 'f';
	else
		itoa(value, tmp, 10);
	return (tmp);
}

static char		*calc_red(int r, char *new)
{
	int		red_hex;
	float	remainder;

	red_hex = r / 16;
	remainder = ((float)r / 16.00) - red_hex;
	remainder = remainder * 16;
	new = ft_strjoin(new, check_value(red_hex));
	new = ft_strjoin(new, check_value(remainder));
	return (new);
}

static char		*calc_green(int g, char *new)
{
	int		green_hex;
	float	remainder;

	green_hex = g / 16;
	remainder = ((float)g / 16.00) - green_hex;
	remainder = remainder * 16;
	new = ft_strjoin(new, check_value(green_hex));
	new = ft_strjoin(new, check_value(remainder));
	return (new);
}

static char		*calc_blue(int b, char *new)
{
	int		blue_hex;
	float	remainder;

	blue_hex = b / 16;
	remainder = ((float)b / 16.00) - blue_hex;
	remainder = remainder * 16;
	new = ft_strjoin(new, check_value(blue_hex));
	new = ft_strjoin(new, check_value(remainder));
	return (new);
}

char			*hv_rgb2hex(int r, int g, int b)
{
	char	*new;

	if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255)
		return (NULL);
	new = ft_strnew(7);
	new[0] = '#';
	new = calc_red(r, new);
	new = calc_green(g, new);
	new = calc_blue(b, new);
	return (new);
}
