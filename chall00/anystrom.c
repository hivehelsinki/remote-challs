/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   anystrom.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: JessicaNystrom <JessicaNystrom@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:33:50 by JessicaNyst       #+#    #+#             */
/*   Updated: 2020/03/23 16:29:18 by JessicaNyst      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_strlen(const char *str)
{
	int		size;

	size = 0;
	while (str[size])
		size++;
	return (size);
}

int		ft_strcmp(const char *s1, const char *s2, int st)
{
	int		i;
	int		len;

	i = 0;
	len = ft_strlen(s1) - 1;
	while (s1[i + st] != '\0' && s2[i] != '\0' && s1[i + st] == s2[i]
			&& i < len)
	{
		i++;
		if (s1[i + st] == '\0' && s2[i] != '\0')
			st -= len + 1;
	}
	return ((unsigned char)s1[i + st] - (unsigned char)s2[i]);
}

int		hv_necklace(char *s1, char *s2)
{
	int		i;
	int		maxtry;

	maxtry = ft_strlen(s1);
	if (maxtry != ft_strlen(s2))
		return (0);
	i = 0;
	while (i <= maxtry)
	{
		if (!ft_strcmp(s1, s2, i))
			return (1);
		i++;
	}
	return (0);
}
