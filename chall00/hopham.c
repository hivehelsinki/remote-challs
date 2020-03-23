/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   hopham.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:43:58 by HoangPham         #+#    #+#             */
/*   Updated: 2020/03/23 16:44:41 by HoangPham        ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *new_str(char *s2_copy)
{
    int     i = 1;
    int     j = 0;
    char    *new;

    new = (char*)malloc(sizeof(char) * (strlen(s2_copy) + 1));
    while (s2_copy[i])
    {
        new[j] = s2_copy[i];
        i++;
        j++;
    }
    new[j] = s2_copy[0];
    new[j + 1] = '\0';
    return (new);
}

int hv_necklace(char *s1, char *s2)
{
    int     i;
    int     j;
    char    *s1_copy;
    char    *s2_copy;
    char    *str;

    if (strlen(s1) != strlen(s2))
        return (0);
    if (strcmp(s1, s2) == 0)
        return (1);
    i = 0;
    while (s1[i] == s2[i])
        i++;
    s1_copy = strdup(&s1[i]);
    s2_copy = strdup(&s2[i]);
    j = strlen(s2_copy);
    i = 0;
    while (i < j)
    {
        str = new_str(s2_copy);
        free(s2_copy);
        s2_copy = strdup(str);
        if (strcmp(s1_copy, str) == 0)
        {
            free(str);
            free(s1_copy);
            free(s2_copy);
            return (1);
        }
        free(str);
        i++;
    }
    free(s1_copy);
    free(s2_copy);
    return (0);
}

int main(void)
{
    int i;

    i = hv_necklace("nicole", "lenico");
    printf("%i\n", i);
}
