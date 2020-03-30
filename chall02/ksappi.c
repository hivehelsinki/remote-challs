#include <string.h>
#include <stdlib.h>

char	*ft_strnew(size_t size)
{
	char	*area;
	size_t	i;

	area = (char *)malloc(sizeof(char) * (size + 1));
	if (!area)
		return (NULL);
	i = 0;
	while (i < size + 1)
	{
		area[i] = '\0';
		++i;
	}
	return (area);
}

char	*ft_itoa_base(unsigned long long nb, char base, char capitalise)
{
	char				*str;
	char				digits[16];
	int					len;
	unsigned long long	nb_copy;

	nb_copy = nb;
	len = 0;
	while ((nb_copy /= base) > 0)
		++len;
	if (base < 2 || base > 16 || !(str = ft_strnew(len + 1)))
		return (NULL);
	if (capitalise)
		memcpy(digits, "0123456789ABCDEF", 16 * sizeof(char));
	else
		memcpy(digits, "0123456789abcdef", 16 * sizeof(char));
	while (len > -1)
	{
		str[len] = digits[nb % base];
		nb /= base;
		--len;
	}
	return (str);
}
int check_if_valid_value(int color)
{
  if (color < 0 || color > 255)
    return 0;
  else
    return 1;
}

char *hv_rgb2hex(int r, int g, int b)
{
  char *ret = (char *)malloc(7);
  char *temp;

  if (!check_if_valid_value(r) || !check_if_valid_value(g) || !check_if_valid_value(b))
  {
    free(ret)
    return NULL;
  }
  strcpy(ret, "#");
  
  temp = ft_itoa_base((unsigned long long)r, (char)16, (char)0);
  if (strlen(temp) == 1)
    strcat(ret, "0");
  strcat(ret, temp);
  free(temp);
  temp = ft_itoa_base((unsigned long long)g, (char)16, (char)0);
  if (strlen(temp) == 1)
    strcat(ret, "0");
  strcat(ret, temp);
  free(temp);
  temp = ft_itoa_base((unsigned long long)b, (char)16, (char)0);
  if (strlen(temp) == 1)
    strcat(ret, "0");
  strcat(ret, temp);
  free(temp);
  return ret;
}