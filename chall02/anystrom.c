/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   anystrom.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: AleXwern <alex.nystrom5@gmail.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 14:11:46 by AleXwern          #+#    #+#             */
/*   Updated: 2020/03/30 14:39:42 by AleXwern         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	ft_firhex(int num, char *rgb, int i)
{
	char	c;

	c = '0';
	if (num < 16)
		rgb[i] = '0';
	else
	{
		num /= 16;
		while (num > 0)
		{
			num--;
			c++;
			if (c == ':')
				c = 'a';
		}
		rgb[i] = c;
	}
}

void	ft_puthex(int num, char *rgb)
{
	char		c;
	static int	i;

	c = '0';
	i++;
	ft_firhex(num, rgb, i);
	num = num % 16;
	while (num > 0)
	{
		num--;
		c++;
		if (c == ':')
			c = 'a';
	}
	i++;
	rgb[i] = c;
}

char	*hv_rgb2hex(int r, int g, int b)
{
	char	*rgb;

	rgb = (char*)malloc(sizeof(char) * 7);
	rgb[0] = '#';
	ft_puthex(r, rgb);
	ft_puthex(g, rgb);
	ft_puthex(b, rgb);
	return (rgb);
}
