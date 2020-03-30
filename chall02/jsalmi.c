#include <stdlib.h>

char puthex(int nb)
{
	char c;

	if (nb >= 10)
	{
		nb == 10 ? c = 'a' : 0;
		nb == 11 ? c = 'b' : 0;
		nb == 12 ? c = 'c' : 0;
		nb == 13 ? c = 'd' : 0;
		nb == 14 ? c = 'e' : 0;
		nb == 15 ? c = 'f' : 0;
	}
	else
		c = nb + '0';
	return (c);
}

char *hv_rgb2hex(int r, int g, int b)
{
	char *final;

	final = (char *)malloc(sizeof(char) * 8);
	final[0] = '#';
	final[7] = '\0';
	final[1] = puthex((unsigned char)r / 16);
	final[2] = puthex((unsigned char)r % 16);
	final[3] = puthex((unsigned char)g / 16);
	final[4] = puthex((unsigned char)g % 16);
	final[5] = puthex((unsigned char)b / 16);
	final[6] = puthex((unsigned char)b % 16);
	return (final);
}
