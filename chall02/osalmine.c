/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   osalmine.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osalmine <osalmine@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 15:43:28 by osalmine          #+#    #+#             */
/*   Updated: 2020/03/30 16:11:43 by osalmine         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int			is_in_range(int n)
{
	if (n < 0 || n > 255)
		return (0);
	return (1);
}

char 		*hv_rgb2hex(int r, int g, int b)
{
	char *hex;

	if (!is_in_range(r) || !is_in_range(g) || !is_in_range(b))
		return (NULL);
	if (!(hex = (char*)malloc(sizeof(char) * 8)))
		return (NULL);
	sprintf(hex, "#%02x%02x%02x", r, g, b);
	return (hex);
}
