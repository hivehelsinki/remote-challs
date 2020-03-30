/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   elindber.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elindber <elindber@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 14:25:39 by elindber          #+#    #+#             */
/*   Updated: 2020/03/30 15:30:38 by elindber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*rgb_itoa_base(char *str, int nbr, int place)
{
	char	*base_str;
	int		count;

	base_str = "0123456789abcdef";
	count = 0;
	while (count < 2)
	{
		str[place] = nbr == 0 ? '0' : base_str[nbr % 16];
		nbr /= 16;
		place--;
		count++;
	}
	return (str);
}

char	*hv_rgb2hex(int r, int g, int b)
{
	char	*rgb_code;

	if (r < 0 || g < 0 || b < 0 || r > 255 || g > 255 || b > 255)
		return (NULL);
	if (!(rgb_code = (char*)malloc(sizeof(char*) * 8)))
		return (NULL);
	rgb_code[0] = '#';
	rgb_code[7] = '\0';
	rgb_code = rgb_itoa_base(rgb_code, b, 6);
	rgb_code = rgb_itoa_base(rgb_code, g, 4);
	rgb_code = rgb_itoa_base(rgb_code, r, 2);
	return (rgb_code);
}
