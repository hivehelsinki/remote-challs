/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sadawi.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sadawi <sadawi@student.hive.fi>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:35:03 by sadawi            #+#    #+#             */
/*   Updated: 2020/03/23 15:03:01 by sadawi           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

char	*ft_strdup(const char *s1)
{
	int		i;
	char	*str;

	if (!s1)
		return (NULL);
	i = 0;
	while (s1[i])
		i++;
	if (!(str = (char*)malloc(i + 1)))
		return (NULL);
	i = 0;
	while (s1[i])
	{
		str[i] = s1[i];
		i++;
	}
	str[i] = '\0';
	return (str);
}

int	ft_strcmp(const char *s1, const char *s2)
{
	int i;

	i = 0;
	while (s1[i] || s2[i])
	{
		if ((unsigned char)s1[i] != (unsigned char)s2[i])
			return ((unsigned char)s1[i] - (unsigned char)s2[i]);
		i++;
	}
	return (0);
}

char	*ft_strnew(size_t size)
{
	char	*str;
	size_t	i;

	if (!(str = (char*)malloc(size + 1)))
		return (NULL);
	i = 0;
	while (i <= size)
	{
		str[i++] = '\0';
	}
	return (str);
}

char	*str_rotate(char *str, int len)
{
	int i;
	char *tmp_str;

	i = 0;
	tmp_str = ft_strnew(len);
	while (i + 1 < len)
	{
		tmp_str[i] = str[i + 1];
		i++;
	}
	tmp_str[i - 1] = str[0];
	free(str);
	return (tmp_str);
}

int	ft_strlen(char *str)
{
	int i;

	i = 0;
	while (str[i++]);
	return (i);
}

int	hv_necklace(char *s1, char *s2)
{
	int i;
	int len;
	char *tmp;

	i = 0;
	len = ft_strlen(s1);
	if (len != ft_strlen(s2))
		return (0);
	if (!ft_strcmp(s1, s2))
		return (1);
	tmp = ft_strdup(s2);
	while (++i < len)
	{
		tmp = str_rotate(tmp, len);
		if (!ft_strcmp(s1, tmp))
		{
			free(tmp);
			return (1);
		}
	}
	free(tmp);
	return (0);
}