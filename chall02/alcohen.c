char *hv_rgb2hex(int r, int g, int b)
{
    char *s;
    char *base16 = "0123456789abcdef";
    int i;

    i = 0;

    s = (char *)malloc(sizeof(char) * 8);
    s[0] = '#';
    s[2] = base16[r % 16];
    r /= 16;
    s[1] = base16[r % 16];
    s[4] = base16[g % 16];
    g /= 16;
    s[3] = base16[g % 16];
    s[6] = base16[b % 16];
    b /= 16;
    s[5] = base16[b % 16];
    s[7] = '\0';
    return (s);
}