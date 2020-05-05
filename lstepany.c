#include <stdio.h>
int ei_i(char *str)
{
  int i;
  int j;

  j = 0;
  i = 0;
  while(str[i] != '\n')
    {
      if(((str[i] == 'e') || (str[i] == 'E')) && ((str[i+1] == 'i') || (str[i+1] == 'I')))
	{
	  j = i + 1;
	}
      i++;
    }
  return(j);
}

int ie_i(char *str)
{
  int i;
  int j;

  i = 0;
  j = 0;
  while(str[i] != '\n')
    {
      if((str[i] == 'i' || str[i] == 'I') && (str[i+1] == 'e' || str[i+1] == 'E'))
	{
	  j = i + 1;
	}
      	  i++;
    }
  return(j);
}

int	ft_ie_except_after_c(char *str)
{
  int ei;
  int ie;

  ei = ei_i(str);
  ie = ie_i(str);
  if ((ei == 0) && (ie == 0))
    return(1);
  if ((ei != 0) && (ie != 0))
    {
      if(((str[ei - 2] == 'c') || (str[ei - 2] == 'C')) && ((str[ie - 2] != 'c') || (str[ie - 2] != 'C')))
    return(1);
    else
      return(0);
    }
if ((ei != 0) && (ie == 0))
  {
    if ((str[ei - 2] == 'c') || (str[ei - 2] == 'C'))
      return(1);
    else
      return(0);
  }
if ((ei == 0) && (ie != 0))
  {
    if((str[ie - 2] == 'c') || (str[ie - 2] == 'C'))
    return(0);
  else
    return(1);
  }
}
