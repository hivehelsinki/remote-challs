/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   jwilen.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jochumwilen <jochumwilen@student.le-101.fr>+#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 21:59:45 by jochumwilen       #+#    #+#             */
/*   Updated: 2020/03/23 21:59:45 by jochumwilen      ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <unistd.h>

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

    j = 0;
    k = 0;
    len_s1 = ft_strlen(s1);
    len_s2 = ft_strlen(s2);
    if (len_s1 != len_s2)
        return (0);
    if (s1 == s2)
        return (1);
    while (s1[j])
    {
        while (s2[k])
        {
            while (s1[j] == s2[k])
            {
                j++;
                k++;
                if (s2[k] == '\0')
                {
                    k = 0;
                }
                if (s1[j] == '\0')
                    return (1);
            }
            k++;
            j = (s1[j-1] == s2[k-1]) ? 0 : j;
        }
        j++;
    }
    return(0);
}