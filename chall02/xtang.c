/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   xtang.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: xtang <xtang@student.hive.fi>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/31 00:49:24 by xtang             #+#    #+#             */
/*   Updated: 2020/03/31 10:30:52 by xtang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdlib.h>

static char	*ft_itoa_base(int value, int base)
{
	char *res;
	char *hex;

	if (!(res = (char *)malloc(sizeof(char) * (2 + 1))))
		return (NULL);
	if (!(hex = (char *)malloc(sizeof(char) * (16 + 1))))
		return (NULL);
	hex = "0123456789abcdef";
	res[0] = hex[value / base];
	res[1] = hex[value % base];
	res[2] = '\0';
	return (res);
}

char		*hv_rgb2hex(int r, int g, int b)
{
	char *res;
	char *str_r;
	char *str_g;
	char *str_b;

	if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255)
		return (NULL);
	if (!(res = (char *)malloc(sizeof(char) * (7 + 1))))
		return (NULL);
	res[0] = '#';
	res[1] = '\0';
	str_r = ft_itoa_base(r, 16);
	str_g = ft_itoa_base(g, 16);
	str_b = ft_itoa_base(b, 16);
	res = strcat(res, str_r);
	res = strcat(res, str_g);
	res = strcat(res, str_b);
	return (res);
}
