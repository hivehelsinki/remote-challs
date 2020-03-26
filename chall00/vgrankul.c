/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   hw_necklace.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vgrankul <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/29 13:50:28 by vgrankul          #+#    #+#             */
/*   Updated: 2019/11/07 15:50:15 by vgrankul         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(const char *str)
{
	int counter;

	counter = 0;
	while (*str != '\0')
	{
		str++;
		counter++;
	}
	return (counter);
}

int check_match(char *s1, char *s2, int i, int j, int k)
{
     while(s2[i] != '\0')
    {
        if (s2[i] == s1[0])
        {
            j = 0;
            k = i;
            while(s1[j] != '\0')
            {
                if(s2[k] == '\0')
                    k = 0;
                if(s1[j] == s2[k])
                {
                    j++;
                    k++;
                }
                else
                    break ;
            }
            if(s1[j] == '\0')
                return(1);
        }
        i++;
    }
    return (0);
}

int hv_necklace(char *s1, char *s2)
{
    int i;
    int j;
    int k;

    i = 0;
    j = 0;
    k = 0;
    if(ft_strlen(s1) != ft_strlen(s2))
        return (0);
    if (s1[0] == '\0' && s2[0] == '\0')
        return (1);
    if (check_match(s1, s2, i, j, k) == 1)
        return (1);
   else
        return(0);
}