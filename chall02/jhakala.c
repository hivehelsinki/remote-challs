#include <stdlib.h>

char get_hex(int i)
{
  if (i > 9)
    return ('a' + i - 10);
  else
    return (i + 48);
}

void put_hex(char *str, int i, int a)
{
  str[i * 2] = get_hex(a % 16);
  if (a > 15)
      str[i * 2 - 1] = get_hex((a / 16) % 16);
  else
      str[i * 2 - 1] = '0';
}

char *hv_rgb2hex(int r, int g, int b)
{
  char *str;
  
  if (!(str = (char*)malloc(sizeof(char) * 8)))
    return (NULL);
  str[0] = '#';
  str[7] = '\0';
  put_hex(str, 1, r);
  put_hex(str, 2, g);
  put_hex(str, 3, b);
  return (str);
}

/*
#include <stdio.h>

int main(void)
{
  printf("%s\n", hv_rgb2hex(252, 186, 3));
  printf("%s\n", hv_rgb2hex(0, 0, 0));
  printf("%s\n", hv_rgb2hex(255, 255, 255));
  printf("%s\n", hv_rgb2hex(16, 16, 16));
  printf("%s\n", hv_rgb2hex(15, 15, 15)); 
  return (0);
}
*/
