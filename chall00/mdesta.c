#include <string.h>

/*
** Rotating the string:
** -> shifts the characters in the string once to the LEFT
** -> the first character becomes the last char in the NEW string
*/

char    *strrot(char *s2)
{
    unsigned int    i;
    char            *temp;

    i = 0;
    temp = strdup(s2);
    while (i < (strlen(s2) - 1))
    {
        s2[i] = temp[i + 1];
        i++;
    }
   s2[i] = temp[0];
   return (s2);
}

/*
** Three Conditions to check before actual comparision
**  1. Do NOT Compare NULL
**  2. Compare only if the strings are SAME Length
**  3. If both strings are empty, return as SAME strings
** A word with n alphabets can be rotated (in a circle)
** to form n - 1 different words
** Hence, COMPARING a maximum of one less the length of
** the first string times is enough
** COMPARE the strings MAX (n - 1) times
** -> if they are the SAME
**      -> return result
** -> if they are DIFFERENT
**      -> rotate second string
** After enough comparision, return result
*/

int hv_necklace(char *s1, char *s2)
{
    int             result;
    unsigned int    i;

    if (!s1 || !s2)
        return (0);
    result = 0 ;
    i = 0;
    if (strlen(s1) != strlen(s2))
        return (0);
    if (strlen(s1) == 0 && strlen(s2)== 0)
        return (1);
    while (i < strlen(s1) && result == 0)
    {
        if (strcmp(s1, s2) == 0)
            result = 1;
        else
            strrot(s2);
        i++;
    }
    return (result);
}