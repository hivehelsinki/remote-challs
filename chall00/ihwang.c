/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ihwang.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ihwang <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:33:38 by ihwang            #+#    #+#             */
/*   Updated: 2020/03/23 15:04:48 by ihwang           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int					ft_strcmp(const char *s1, const char *s2)
{
	unsigned char	*pt_s1;
	unsigned char 	*pt_s2;

	pt_s1 = (unsigned char*)s1;
	pt_s2 = (unsigned char*)s2;
	while (*pt_s1 || *pt_s2)
	{
		if (*pt_s1 > *pt_s2)
			return (1);
		else if (*pt_s1 < *pt_s2)
			return (-1);
		pt_s1++;
		pt_s2++;
	}
	return (0);
}

int					ft_strlen(char *str)
{
	int				i;

	i = -1;
	while (str[++i])
		NULL;
	return (i);
}

char				**make_examples(char *s1, int nb)
{
	int				i, j, k, l;
	char			**ret;

	ret = (char**)malloc(sizeof(char*) * nb);
	i = -1;
	while (++i < nb)
	{
		ret[i] = (char*)malloc(nb + 1);
		j = -1;
		k = i - 1;
		l = -1;
		while (++j < nb)
		{
			if (++k < nb)
				ret[i][j] = s1[k];
			else
				ret[i][j] = s1[++l];
		}
	}
	return (ret);
}

void				ft_strlst_del(char **str, int nb)
{
	int				i;

	i = -1;
	while (++i < nb)
		free(str[i]);
	free(str);
}

int					hv_necklace(char *s1, char *s2)
{
	int				nb;
	char			**psb_cases;
	int				i;

	nb = ft_strlen(s1);
	if (!nb && !ft_strlen(s2))
		return (1);
	psb_cases = make_examples(s1, nb);
	i = -1;
	while (++i < nb)
		if (!ft_strcmp(psb_cases[i], s2))
		{
			ft_strlst_del(psb_cases, nb);
			return (1);
		}
	ft_strlst_del(psb_cases, nb);
	return (0);
}
