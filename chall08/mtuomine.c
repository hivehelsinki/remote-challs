#define _GNU_SOURCE
#include <string.h>

static int c_found(char *str) {
	char c = *(str - 1);
	return (c && (c == 'c' || c == 'C'));
}

int ft_ie_except_after_c(char *str) {
	char *ei_found = strcasestr(str, "ei");
	char *ie_found = strcasestr(str, "ie");
	if ((ei_found == 0 && ie_found == 0) || (ei_found && c_found(ei_found)) || (ie_found && !c_found(ie_found)))
		return (1);
	return 0;
}
