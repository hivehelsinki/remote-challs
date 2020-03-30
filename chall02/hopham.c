/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   hopham.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/30 15:23:25 by HoangPham         #+#    #+#             */
/*   Updated: 2020/03/30 17:16:12 by HoangPham        ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include "ft_itoa_base.c"

char *hv_rgb2hex(int r, int g, int b)
{
    char    *hex_str;
    char    *first_str;
    char    *convert;
    char    *sec_str;

    if ((r < 0 || g < 0 || b < 0) || (r > 255 || g > 255 || b > 255))
        return (NULL);
    convert = ft_itoa_base(r, 16);
    first_str = ft_strjoin("#", convert);
    convert = ft_itoa_base(g, 16);
    sec_str = ft_strjoin(first_str, convert);
    free(first_str);
    convert = ft_itoa_base(b, 16);
    hex_str = ft_strjoin(sec_str, convert);
    free(sec_str);
    return (hex_str);
}
