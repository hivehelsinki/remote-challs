/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   wkorande.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wkorande <wkorande@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 14:21:32 by wkorande          #+#    #+#             */
/*   Updated: 2020/03/30 14:38:04 by wkorande         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

static int in_range(int n)
{
	if (n < 0 || n > 255)
		return (0);
	return (1);
}

char *hv_rgb2hex(int r, int g, int b)
{
	char *buf;

	if (!in_range(r) || !in_range(g) || !in_range(b))
		return (NULL);
	if (!(buf = (char*)malloc(sizeof(char) * 8)))
		return (NULL);
	sprintf(buf, "#%02x%02x%02x", r, g, b);
	return (buf);
}
