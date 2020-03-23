/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ykalashn.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ykalashn <ykalashn@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 16:36:54 by ykalashn          #+#    #+#             */
/*   Updated: 2020/03/23 16:37:09 by ykalashn         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

int     hv_necklace(char *s1, char *s2)
{
    int i;
    int j;

    j = 0;
    i = 0;
    while (strlen(s1) == strlen(s2) && s1[i] && s2[j])
    {
        while(s2[j])
        {
            if (s1[i+1] == '\0' && s1[i] != s2[j])
                return 0;
            if (s1[i] == s2[j])
                j++;
            if (s1[i+1] == '\0' && s1[i] == s2[j-1] && s2[j])
            {
                i = 0;
                j++;
            }
            if (s2[j] == '\0')
                return 1;
            i++;
        }
    }
    return 0;
}
