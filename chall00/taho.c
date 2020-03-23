/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   taho.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: taho <taho@student.hive.fi>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 15:38:48 by taho              #+#    #+#             */
/*   Updated: 2020/03/23 16:22:30 by taho             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdlib.h>

void	rotate_string(char *s, int len)
{
    char	tmp;
    int		i;

    tmp = s[0];
    i = -1;
    while (++i < len - 1)
        s[i] = s[i + 1];
    s[i++] = tmp;
    s[i] = '\0';
}

/*
** ------------------------------- HV_NECKLACE ------------------------------ **
*/

int hv_necklace(char *s1, char *s2)
{
    char	*copy;
	int		len;
    int		i;

	len = strlen(s1);
    if (len == strlen(s2))
    {
		copy = (char *)malloc(sizeof(char) * (len + 1));
		strcpy(copy, s1);
        i = -1;
        while (++i < len)
        {
            rotate_string(copy, len);
            if (strcmp(copy, s2) == 0)
			{
				free(copy);
				return (1);
			}  
        }
    }
	free(copy);
    return (0);
}
