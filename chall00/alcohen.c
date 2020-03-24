#include <stdlib.h>

int len(char *s)
{
    int i = 0;
    while (s[i])
        i++;
    return (i);
}

int hv_necklace(char *s1, char *s2)
{
    char *new;
    int i;
    int j;
    int count;
    int highest;

    i = 0;
    j = 0;
    if (len(s1) != len(s2))
        return (0);
    new = (char *)malloc(sizeof(char) * len(s1) * 2 + 1);
    while (s1[i])
    {
        new[i] = s1[i];
        new[i+len(s1)] = s1[i];
        i++;
    }
    i = 0;
    count = 0;
    highest = 0;
    while (new[i])
    {
        j = 0;
        count = 0;
        while (s2[j])
        {
            if (s2[j] == new[i+j])
            {
                count++;
                if (highest < count)
                    highest = count;
            }
            j++;
        }
        i++;
    }
    return (highest == len(s1));
}