/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   jwilen.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jochumwilen <jochumwilen@student.le-101.fr>+#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 21:59:45 by jochumwilen       #+#    #+#             */
/*   Updated: 2020/03/24 10:05:56 by jochumwilen      ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

int     ft_strlen(char *str)
{
    int     i;

    i = 0;
    while (str[i])
        i++;
    return (i);
}

int     hv_necklace(char *s1, char *s2)
{
    int     len_s1;
    int     len_s2;
    int     j;
    int     k;
    int		s;

    j = 0;
    s = 0;
    len_s1 = ft_strlen(s1);
    len_s2 = ft_strlen(s2);
    if (len_s1 != len_s2)
        return (0);
    if (s1 == s2)
        return (1);
    while (s2[s])
	{
    	k = s;
    	while (s1[j] == s2[k])
    	{
    		j++;
    		k++;
    		if (s2[k] == '\0')
    			k = 0;
    		if (s1[j] == '\0')
    			return (1);
    	}
    	s++;
    	j = 0;
	}
    return(0);
}