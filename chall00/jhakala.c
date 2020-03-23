int ft_strlen(char *str)
{
  int i;
  
  i = 0;
  while (str[i])
    i++;
  return (i);
}

int hv_necklace(char *s1, char *s2)
{
  int tmp;
  int j;
  int j_len;
  
  if (!s1 && !s2)
    return (1);
  if (!s1 || !s2 || (j_len = ft_strlen(s2)) != ft_strlen(s1))
    return (0);
  tmp = 0;
  while (tmp < j_len)
  {
    j = tmp;
    while (s1[0] != s2[j] && s2[j])
      j++;
    tmp = j;
    while (s1[j - tmp] == s2[j] && s1[j - tmp] && s2[j])
      j++;
    if (!s2[j])
    {
      j = 0;
      while (s1[j_len - tmp + j] == s2[j] && s1[j_len - tmp + j] && s2[j])
        j++;
      break ;
    }
    tmp++;
  }
  if (tmp >= j_len)
    return (0);
  if (!s1[j_len - tmp + j])
    return (1);
  return (0);
}
