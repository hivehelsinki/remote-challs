/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   try2.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lsjoberg <lsjoberg@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 23:39:57 by lsjoberg          #+#    #+#             */
/*   Updated: 2020/03/24 11:02:14 by lsjoberg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int	hv_necklace(char *s1, char *s2)
{
	int		i = 0;
	int		j = 0;
	if (s1[i] == '\0' && s2[i] == '\0')
		return (1);
	while (s1[i] || s1[i] == '\0' || s2[i] == '\0')
	{
		if ((s1[i] == '\0' && s2[i] != '\0') ||
			(s2[i] != '\0' && s2[i] == '\0'))
				return (0);
		else if (s1[i] == '\0' && s2[i] == '\0')
			break ;
		else
		i++;
	}
	i = 0;
	while (s1[i] != s2[j])
		j++;
	while (s1[i])
	{
		if (s1[i] == '\0')
			return (1);
		else if (s2[j] == '\0')
			j = 0;
		else if (s1[i] != s2[j])
		{
				j++;
				break ;
		}
		else
		{
			i++;
			j++;
			if (s1[i] == '\0')
				return (1);
			continue;
		}
	}
	return (0);
}
