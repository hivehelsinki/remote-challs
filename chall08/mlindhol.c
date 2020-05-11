/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mlindhol.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mlindhol <mlindhol@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/05/05 09:10:27 by mlindhol          #+#    #+#             */
/*   Updated: 2020/05/05 09:10:27 by mlindhol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int     ft_ie_except_after_c(char *str)
{
    int     i;

    i = 0;
    if (!str)
        return (0);
    while (str[i] && str[i + 1])
    {
        if (str[i] == 'e' && str[i + 1] == 'i' && str[i - 1] != 'c')
            return (0);
        if (str[i] == 'i' && str[i + 1] == 'e' && str[i - 1] == 'c')
            return (0);
        ++i;
    }
    return (1);
}