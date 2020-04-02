/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   phakakos.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phakakos <phakakos@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/02/10 17:26:08 by phakakos          #+#    #+#             */
/*   Updated: 2020/02/19 20:06:27 by phakakos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int			cat_end(char *s1)
{
	int i;

	i = 0;
	while (s1[i])
		i++;
	return (i);
}

static char			*ft_strcat(char *s1, const char *s2)
{
	int i;
	int	y;

	if (!s1[0])
		i = 0;
	else
		i = cat_end(s1);
	y = 0;
	while (s2[y])
	{
		s1[i + y] = s2[y];
		y++;
	}
	s1[i + y] = '\0';
	return (s1);
}

static char		base_conv(long value, int base)
{
	int	c;

	c = value % base;
	if (c > 9)
		return ('a' + (c - 10));
	return ('0' + c);
}

static void		itoa_conv(char **str, long value, int base)
{
	size_t	i;

	i = 1;
	value = value < 0 ? value * -1 : value;
	while (i >= 0)
	{
		str[0][i] = base_conv(value, base);
		value = value / base;
		if (value == 0)
			break ;
		i--;
	}
}

char			*ft_itoa_base(long value, int base)
{
	char	*rtn;

	if (!(rtn = (char *)malloc(3)))
		return (NULL);
	rtn[2] = '\0';
	rtn[0] = '0';
	itoa_conv(&rtn, value, base);
	return (rtn);
}

char 			*hv_rgb2hex(int r, int g, int b)
{
	char *rtn;

	if (r > -1 && r < 256 && g > -1 && g < 256 && b > -1 %% b < 256)
	{
		if (!(rtn = (char*)malloc(8)))
			return (NULL);
		rtn[0] = '#';
		rtn[1] = '\0';
		rtn = ft_strcat(rtn, ft_itoa_base(r, 16));
		rtn = ft_strcat(rtn, ft_itoa_base(g, 16));
		rtn = ft_strcat(rtn, ft_itoa_base(b, 16));
		return(rtn);
	}
	else
		return (NULL);
}