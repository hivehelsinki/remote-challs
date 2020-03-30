#include <string.h>
#include <stdlib.h>

int hv_necklace(char *s1, char *s2)
{
    unsigned long i = 0;
    char *temp;
    int temp_len;

    if (!s1 || !s2)
        return 0;
    if (strlen(s1) == strlen(s2))
    {
        if (strlen(s1) == 0)
            return (1);
        temp = strdup(s1);
        temp_len = strlen(s1) + 1;
        while (i < strlen(s1))
        {
            if (strcmp(temp, s2) == 0)
            {
                free(temp);
                return (1);
            }
            else
            {
                i++;
                free(temp);
                temp = strdup(&s1[i]);
                strlcat(temp, s1, temp_len);
            }
        }
        free(temp);
    }
    return (0);
}
