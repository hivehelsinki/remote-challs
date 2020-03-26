/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mlindhol.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mlindhol <mlindhol@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:32:37 by mlindhol          #+#    #+#             */
/*   Updated: 2020/03/23 14:32:37 by mlindhol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>

int     hv_necklace(char *s1, char *s2)
{
    int     len1;    
    int     len2;
    int     i;
    int     j;

    len1 = strlen(s1);
    len2 = strlen(s2);
    i = 0;
    j = -1;

    if (s1 == s2)
        return (1);
    if (len1 != len2)
        return (0);
    if (!strchr(s2, s1[0]))
        return (0);
    while (++j < len2)
    {
        while (s1[i] != '\0' && s2[j] != '\0' && s1[i] == s2[j])
        {
            ++i;
            ++j;
            if (s1[i] != '\0' && s2[j] == '\0')
            {
                j = 0;
                if (s1[i] != s2[j])
                    return (0);
            }
            if (s1[i] == '\0')
                return (1);
        }
        i = 0;
    }
    return (0);
}
