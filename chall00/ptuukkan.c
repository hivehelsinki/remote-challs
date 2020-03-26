/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ptuukkan.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptuukkan <ptuukkan@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:51:53 by ptuukkan          #+#    #+#             */
/*   Updated: 2020/03/23 14:51:54 by ptuukkan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char	*ft_strdup(const char *s1)
{
	char	*dupstr;
	int		i;

	dupstr = (char *)malloc(sizeof(char) * strlen(s1) + 1);
	i = 0;
	if (dupstr)
	{
		while (s1[i] != '\0')
		{
			dupstr[i] = s1[i];
			i++;
		}
		dupstr[i] = '\0';
		return (dupstr);
	}
	else
		return (NULL);
}

void	slide(char **s1, char *s2, int len)
{
	char	tmp;
	int		i;

	tmp = **s1;
	i = 0;
	while (i + 1 < len)
	{
		(*s1)[i] = (*s1)[i + 1];
		i++;
	}
	(*s1)[i] = tmp;
}

int		hv_necklace(char *s1, char *s2)
{
	int	len;
	int	i;

	if (*s1 == '\0' && *s2 == '\0')
		return (1);
	len = strlen(s1);
	i = 0;
	s1 = ft_strdup(s1);
	if (s1 == NULL)
		return (0);
	while (i < len)
	{
		if (strcmp(s1, s2) == 0)
			return (1);
		slide(&s1, s2, len);
		i++;
	}
	return (0);
}
