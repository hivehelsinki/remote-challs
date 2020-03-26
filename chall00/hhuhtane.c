/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   hhuhtane.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hhuhtane <hhuhtane@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:55:04 by hhuhtane          #+#    #+#             */
/*   Updated: 2020/03/23 15:27:21 by hhuhtane         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int		ft_strlen(char *str)
{
	int 	i;

	i = 0;
	while (str && str[i])
		i++;
	return (i);
}

int		hv_necklace(char *s1, char *s2)
{
	int		i1;
	int		i2;
	int		len;

	i1 = 0;
	i2 = 0;
	len = ft_strlen(s1);
	if (ft_strlen(s2) != len)
		return (0);
	while (s1[i1] != s2[i2] && i2 != len)
		i2++;
	while (i2 < len)
	{
		if (s1[i1++] != s2[i2++])
			return (0);
	}
	i2 = 0;
	while (i1 < len)
	{
		if (s1[i1++] != s2[i2++])
			return (0);
	}
	return (1);
}
