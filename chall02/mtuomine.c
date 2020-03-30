#include <stdio.h>
#include <stdlib.h>

#define ARR_LEN 3
#define HEX_LEN 7
#define MIN_VALUE 0
#define MAX_VALUE 255

static int is_valid(int arr[ARR_LEN])
{
	size_t i = 0;
	while (i < ARR_LEN)
	{
		if (arr[i] < MIN_VALUE || arr[i] > MAX_VALUE)
			return 0;
		i++;
	}
	return 1;
}

char *hv_rgb2hex(int r, int g, int b)
{
	int arr[ARR_LEN] = {r, g, b};

	if (!is_valid(arr))
		return NULL;

	char *hex = (char *)malloc((sizeof(char) * HEX_LEN) + 1);
	if (!hex)
		return NULL;

	sprintf(hex, "%s%02x%02x%02x", "#", r, g, b);
	hex[HEX_LEN] = '\0';
	return hex;
}
