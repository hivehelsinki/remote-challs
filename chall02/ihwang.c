/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ihwang.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ihwang <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 14:13:25 by ihwang            #+#    #+#             */
/*   Updated: 2020/03/30 14:55:20 by ihwang           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdlib.h>

static char	conv_to_hex(int *color)
{
	char	ret;
	int		cp;

	cp = *color % 16;
	*color /= 16;
	if (cp == 10)
		ret = 'a';
	else if (cp == 11)
		ret = 'b';
	else if (cp == 12)
		ret = 'c';
	else if (cp == 13)
		ret = 'd';
	else if (cp == 14)
		ret = 'e';
	else if (cp == 15)
		ret = 'f';
	else
		ret = cp + 48;
	return (ret);
}

void		add_chars(char *ret, int color, int index)
{
	ret[index] = conv_to_hex(&color);
	ret[index - 1] = conv_to_hex(&color);
}

char		*hv_rgb2hex(int r, int g, int b)
{
	char	*ret;

	if (r > 255 || g > 255 || b > 255)
		return (NULL);
	if (r < 0 || g < 0 || b < 0)
		return (NULL);
	if (!(ret = (char*)malloc(sizeof(char) * 8)))
		return (NULL);
	bzero(ret, 8);
	ret[0] = '#';
	ret[7] = '\0';
	add_chars(ret, r, 2);
	add_chars(ret, g, 4);
	add_chars(ret, b, 6);
	return (ret);
}
