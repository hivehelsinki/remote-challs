/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   taho.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: taho <taho@student.hive.fi>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 15:38:48 by taho              #+#    #+#             */
/*   Updated: 2020/03/23 16:52:05 by taho             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdlib.h>

/*
** ----------------------------- ROTATE_STRING ------------------------------ **
** Rotate a string one letter to the left (first letter becomes last).
*/

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
** Take two strings as arguments.
** Goal is to see if s1 can be rotated so that it equals s2.
** If strings are not equal length, return 0.
** Make a copy of s1 (because arguments are read-only string literals).
** Rotate the copy one step and return 1 if it equals s2.
** Keep doing it until you have rotated each letter.
** If there was no match, return 0.
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
