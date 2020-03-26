#include <stdlib.h>

int     ft_strlen(char *s)
{
    int i;

    i = 0;
    while (s[i] != '\0')
        i++;
    return (i);
}

char	*ft_strdup(char *str)
{
	char	*dup;
	int		i;

	i = 0;
	if (!(dup = (char *)malloc(sizeof(char) * (ft_strlen(str) + 1))))
		return (NULL);
	while (str[i] != '\0')
	{
		dup[i] = str[i];
		i++;
	}
	dup[i] = '\0';
	return (dup);
}

int	ft_strcmp(const char *s1, const char *s2)
{
	int i;

	i = 0;
	while (s1[i] == s2[i] && s1[i] && s2[i])
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

char    *ft_pushback(char *s, int len)
{
    int     i;
    char    *s2;
    char    *s1;

    s1 = ft_strdup(s);
    if (!(s2 = (char *)malloc(sizeof(char) * (len + 1))))
        return (NULL);
    i = 0;
    while (i < len - 1)
    {
        s2[i] = s1[i + 1];
        i++;
    }
    s2[len - 1] = s1[0];
    s2[len] = '\0';
    free(s1);
    return (s2);
}

int     hv_necklace(char *s1, char *s2)
{
    int     len1;
    int     len2;
    char    *tmp;
    int     i;

    len1 = ft_strlen(s1);
    len2 = ft_strlen(s2);
    i = 0;
    if (len1 == len2 && len1 == 0)
        return (1);
    if (len1 == len2)
    {
        while (i < len1)
        {
            if (ft_strcmp(s1, s2) == 0)
            {
                if (i > 0)
                    free(s2);
                return (1);
            }
            tmp = s2;
            s2 = ft_pushback(tmp, len1);
            if (i > 0)
                free(tmp);
            i++;
        }
    }
    return (0);
}
