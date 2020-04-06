/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mlindhol.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mlindhol <mlindhol@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 14:21:19 by mlindhol          #+#    #+#             */
/*   Updated: 2020/03/30 14:21:19 by mlindhol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

char	*hv_rgb2hex(int r, int g, int b)
{
	char	*ret;

	if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255)
		return (NULL);
	if (!(ret = (char*)malloc(sizeof(char) * 8)))
		return (NULL);
	sprintf(ret, "#%02x%02x%02x", r, g, b);
	return (ret);
}
