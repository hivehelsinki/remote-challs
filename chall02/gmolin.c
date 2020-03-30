/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   gmolin.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmolin <gmolin@student.hive.fi>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 16:04:38 by gmolin            #+#    #+#             */
/*   Updated: 2020/03/30 16:33:33 by gmolin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

char		*hv_rgb2hex(int r, int g, int b)
{
	char	*str;
	int		array[3] = {r, g, b};
	int 	i;

	i = 0;
	while (i < 3)
	{
		if (array[i] < 0 || array[i] > 255)
			return (NULL);
		i++;
	}
	if (!(str = (char*)malloc(sizeof(char) * 8)))
		return (NULL);
	sprintf(str, "#%02x%02x%02x", r, g, b);
	return (str);
}