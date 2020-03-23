#include <stdlib.h>

size_t	ft_strlen(const char *s)
{
	size_t	c;

	c = 0;
	while (s[c] != '\0')
		c++;
	return (c);
}

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	if (n == 0)
		return (0);
	while (*s1 && *s1 == *s2 && --n)
	{
		s1++;
		s2++;
	}
	return (*(unsigned char*)s1 - *(unsigned char *)s2);
}

int hv_necklase(char *s1, char *s2)
{
    int len;
    int lentwo;
    int offset;

    if (!(s1 || s2))
        return (0);
    len = ft_strlen(s1);
    lentwo = ft_strlen(s2);
    if (lentwo != len)
        return (0);
    if (len == 0 && lentwo == 0)
        return (1);
    offset = 0;
    while (len - offset)
    {
        if (ft_strncmp(s1, &s2[offset], len - offset) == 0
        && ft_strncmp(&s1[len - offset], s2, offset) == 0)
            return (1);
        offset++;
    }
    return (0);
}