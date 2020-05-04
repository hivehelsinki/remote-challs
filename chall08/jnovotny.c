/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   jnovotny.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/05/04 18:14:56 by jnovotny          #+#    #+#             */
/*   Updated: 2020/05/04 18:50:49 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>

int ft_ie_except_after_c(char *str)
{
	int i;
	
	if (strlen(str) >= 2 && str[0] == 'e' && str[1] == 'i')
		return 0;
	else if (strlen(str) < 3 || (!strstr(str, "ei") && !strstr(str, "ie")))
		return 1;
	i = 1;
	while (str[i + 1] != '\0')
	{
		if (str[i] == 'e' && str[i + 1] == 'i' && str[i - 1] != 'c')
			return 0;
		else if (str[i] == 'i' && str[i + 1] == 'e' && str[i - 1] == 'c')
			return 0;
		else
			i++;
	}
	return 1;
}