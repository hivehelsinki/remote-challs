/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   wkorande.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wkorande <wkorande@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:55:56 by wkorande          #+#    #+#             */
/*   Updated: 2020/03/23 14:56:08 by wkorande         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <string.h>

int	hv_necklace(char *s1, char *s2)
{
	int l1;
	int l2;
	int i;
	int off;

	l1 = strlen(s1);
	l2 = strlen(s2);
	if (l1 != l2)
		return (0);
	off = l2 - strlen(strchr(s2, s1[0]));
	i = 0;
	while (i < l2)
	{
		if (s1[i] != s2[(off + i) % l2])
			return (0);
		i++;
	}
	return (1);
}


