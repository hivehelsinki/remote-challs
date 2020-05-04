int		ft_ie_except_after_c(char *str)
{
	return (!str || !str[0] || !str[1] || !str[2]
	|| (!(str[1] == 'i' && str[2] == 'e' && str[0] == 'c')
	&& !(str[1] == 'e' && str[2] == 'i' && str[0] != 'c')
	&& ft_ie_except_after_c(str + 1)));
}