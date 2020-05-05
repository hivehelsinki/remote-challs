/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   xtang.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: xtang <xtang@student.hive.fi>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/05/05 11:30:48 by xtang             #+#    #+#             */
/*   Updated: 2020/05/05 15:59:39 by xtang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_ie_except_after_c(char *str)
{
	int i;

	i = 0;
	while (str[i] != '\0' || str[i] != 'e')
	{
		if (str[i] == '\0')
			return (1);
		if (str[i] == 'e')
			break ;
		i++;
	}
	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] == 'e')
		{
			if (str[i - 2] == 'c' && str[i - 1] == 'i')
				return (0);
			if (str[i - 1] == 'c' && str[i + 1] == 'i')
				return (1);
			if (str[i - 1] == 'i' && str[i - 1] != 'c')
				return (1);
			return (1);
		}
		i++;
	}
	return (0);
}
