/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/01/07 10:25:39 by HoangPham         #+#    #+#             */
/*   Updated: 2020/03/30 17:08:54 by HoangPham        ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*str;
	int		i;
	int		j;

	if (!s1 || !s2)
		return (NULL);
	str = (char*)malloc(sizeof(char) * (strlen(s1) + strlen(s2) + 1));
	if (str == NULL)
		return (NULL);
	i = 0;
	j = 0;
	while (s1[i])
	{
		str[i] = s1[i];
		i++;
	}
	while (s2[j])
	{
		str[i] = s2[j];
		i++;
		j++;
	}
	free((void*)s2);
	str[i] = '\0';
	return (str);
}

int		get_len(int value, int base)
{
	int	i;

	i = 0;
	while (value)
	{
		value = value / base;
		i++;
	}
	return (i);
}

char	*ft_strnew(int len)
{
	char	*str;

	str = (char*)malloc(sizeof(char) * (len + 1));
	while (len >= 0)
	{
		str[len] = '\0';
		len--;
	}
	return (str);
}

char	ft_calculate_char(int mod)
{
	char	return_char;

	return_char = '0';
	while (mod)
	{
		return_char++;
		mod--;
		if (return_char == ':')
			return_char = 'a';
	}
	return (return_char);
}

char	*ft_itoa_base(int value, int base)
{
	char	*str;
	int		mod;
	int		len;
	int		original_value;

	if (value == 0)
	{
		str = ft_strnew(2);
		str[0] = '0';
		str[1] = '0';
		return (str);
	}
	original_value = value;
	len = get_len(value, base);
	str = ft_strnew(len);
	len--;
	while (value > 0)
	{
		mod = value % base;
		value = value / base;
		str[len] = ft_calculate_char(mod);
		len--;
	}
	if (original_value <= 9)
		str = ft_strjoin("0", str);
	return (str);
}
