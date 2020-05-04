#define _GNU_SOURCE
#include <string.h>

static int c_found(char *str) {
	if (!str || !(str-1))
		return (0);
	char c = *(str - 1);
	return (c && (c == 'c' || c == 'C'));
}

int ft_ie_except_after_c(char *str) {
	if (!str)
		return (1);

	char *ei_found = strcasestr(str, "ei");
	char *ie_found = strcasestr(str, "ie");

	if (ei_found == 0 && ie_found == 0) {
		return (1);
	}

	if ((ei_found && !c_found(ei_found)) || (ie_found && c_found(ie_found))) {
		return (0);
	}

	if ((ei_found && c_found(ei_found)) || (ie_found && !c_found(ie_found))) {
		size_t ei_len = (ei_found) ? strlen(ei_found) : 0;
		size_t ie_len = (ie_found) ? strlen(ie_found) : 0;
		if (ei_len) {
			return ft_ie_except_after_c(str+=2);
		} else if (ie_len){
			return ft_ie_except_after_c(str+=2);
		}
	}
	return (1);
}
