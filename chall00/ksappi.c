#include <string.h>

int hv_necklace(char *str1, char *str2)
{
    if (strlen(str1) != strlen(str2))
        return 0;
    if (!strlen(str1) && !strlen(str2))
        return 1;
    char *s2 = strdup(str2);
    for (int i = 1; i <= strlen(str1); ++i)
    {
        if (!strcmp(str1, s2))
            return 1;
        else
        {
            strcpy(s2, &str2[i]);
            strncat(s2, str2, i);
        }
    }
    return 0;
}