#include <stdlib.h>

int     ft_strlen(char *str)
{
    int     i;

    i = 0;
    while (str[i])
        i++;
    return (i);
}

int		ft_strcmp(const char *s1, const char *s2)
{
	while (*s1 == *s2 && *s1 && *s2)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

void    *moveone(char *str)
{
  int   i;
  char *pt;
  
  i = 0;
  pt = malloc(sizeof(char *) * ft_strlen(str));
  while (str[i + 1])
  {
    pt[i] = str[i + 1];
    i++;
  }
  pt[i] = str[0];
  pt[i + 1] = '\0';
  return (pt);
}

int     hv_necklace(char *s1, char *s2)
{
    int   i;
    int   r;
    
    i = 0;
    r = ft_strlen(s1);
    if (!s1 && !s2 || ft_strcmp(s1, s2) == 0)
      return (1);
    else if (!s1 || !s2 || (r != ft_strlen(s2)))
      return (0);
    while (i < r)
    {
      if (ft_strcmp(s1, s2) == 0)
        return (1);
      s2 = moveone(s2);
      i++;
    }
    return (0);
}