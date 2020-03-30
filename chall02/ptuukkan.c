/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ptuukkan.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptuukkan <ptuukkan@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 14:03:53 by ptuukkan          #+#    #+#             */
/*   Updated: 2020/03/30 14:27:54 by ptuukkan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

static char	itoc(int i)
{
	if (i < 10)
		return (i + '0');
	return (i + 87);
}

char		*hv_rgb2hex(int r, int g, int b)
{
	static char	rgb[8];

	if (r > 255)
		r = 255;
	else if (r < 0)
		r = 0;
	if (g > 255)
		g = 255;
	else if (g < 0)
		g = 0;
	if (b > 255)
		b = 255;
	else if (b < 0)
		b = 0;
	rgb[0] = '#';
	rgb[1] = itoc(r / 16);
	rgb[2] = itoc(r % 16);
	rgb[3] = itoc(g / 16);
	rgb[4] = itoc(g % 16);
	rgb[5] = itoc(b / 16);
	rgb[6] = itoc(b % 16);
	rgb[7] = '\0';
	return (rgb);
}
