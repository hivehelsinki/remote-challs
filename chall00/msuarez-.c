/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   msuarez-.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: msuarez- <msuarez-@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:25:43 by msuarez-          #+#    #+#             */
/*   Updated: 2020/03/23 14:25:43 by msuarez-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

static int		ft_strlen(const char *str)
{
	int		i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

static int		ft_strequ(char const *s1, char const *s2)
{
	unsigned int i;

	if (!s1 || !s2)
		return (0);
	if (ft_strlen(s1) != ft_strlen(s2))
		return (0);
	i = 0;
	while (s1[i])
	{
		if (s1[i] == s2[i])
			i++;
		else
			return (0);
	}
	return (1);
}

static void		*first_to_next(char *str)
{
	int		i;
	char	tmp;

	i = 0;
	tmp = str[0];
	while (str[i + 1])
	{
		str[i] = str[i + 1];
		i++;
	}
	str[i] = tmp;
}

int				hv_necklace(char *s1, char *s2)
{
	int		i;

	i = 0;
	if (!s1 || !s2)
		return (0);
	while (i < ft_strlen(s1))
	{
		if (ft_strequ(s1, s2) == 0)
			first_to_next(s2);
		i++;
	}
	if (ft_strequ(s1, s2) == 1)
		return (1);
	return (0);
}
