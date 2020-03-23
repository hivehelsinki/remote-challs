/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   elindber.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elindber <elindber@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 16:02:15 by elindber          #+#    #+#             */
/*   Updated: 2020/03/23 16:17:28 by elindber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdlib.h>

char	*push_right(char *str, int len)
{
	char	*rotated;
	int		i;
	
	i = 0;
	rotated = (char*)malloc(sizeof(char) * (len + 1));
	while (i < len)
	{
		if (i == len - 1)
		{
			rotated[0] = str[i];
			break ;
		}
		rotated[i + 1] = str[i];
		i++;
	}
	rotated[len] = '\0';
	return (rotated);
}

int		hv_necklace(char *s1, char *s2)
{
	unsigned long		len1;
	unsigned long		count;
	
	if (s1 == NULL && s2 == NULL)
		return (1);
	if (!s1 || !s2)
		return (0);
	len1 = strlen(s1);
	count = 0;
	if (strlen(s2) != len1)
		return (0);
	while (count < len1 || (count == 0 && len1 == 0))
	{
		if (strcmp(s1, s2) == 0)
			return (1);
		s1 = push_right(s1, len1);
		count++;
	}
	return (0);
}
