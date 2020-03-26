/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   necklace.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:32:36 by jnovotny          #+#    #+#             */
/*   Updated: 2020/03/23 14:32:36 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

static int  ft_strlen(const char *str)
{
	int i;

	i = 0;
	while (str[i])
		i++;
	return i;
}

int hv_necklace(char *s1, char *s2)
{
	int i;
	int l;
	int start;
	int k;

	l = ft_strlen(s1);
	if (l != ft_strlen(s2))
		return (0);
	else if (l == 0 && ft_strlen(s2) == 0)
		return (1);
	start = 0;
	while (start < l)
	{
		i = start;
		k = 0;
		while (k < l && s1[i] == s2[k])
		{
			i++;
			k++;
			if (i == l && start != 0)
				i = 0;
		}
		if (k == l)
			return (1);
		start++;
	}
	return (0);
}