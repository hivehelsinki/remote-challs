package main

//#include<../chall02/ohakola.c>
//#include<stdlib.h>
//#include <ctype.h>
// char	*parse_rgb_int(char *str, int *nb)
// {
// 	while (!isdigit(*str))
// 		str++;
// 	*nb = atoi(str);
// 	while (isdigit(*str))
// 		str++;
//	return str;
// }
// char 	*body_to_hex(char *str, int *id) {
//	char *res;
// 	int r, g, b;
//
// 	str = parse_rgb_int(str, id);
// 	str = parse_rgb_int(str, &r);
// 	str = parse_rgb_int(str, &g);
// 	str = parse_rgb_int(str, &b);
//  res = hv_rgb2hex(r, g, b);
// 	return res + 1;
// }
import "C"
import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func http_get(client http.Client, url string) (string, bool) {
	log.Println("Getting: " + url)
	resp, err := client.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	log.Println(
		fmt.Sprintf("Response status: %d", resp.StatusCode),
	)
	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			log.Fatal(err)
		}
		bodyString := string(bodyBytes)
		log.Println(
			fmt.Sprintf("Response body %s", bodyString),
		)
		return bodyString, true
	}
	return "", false
}

func main() {
	log.SetFlags(log.Lmicroseconds)
	url := "https://chall03.hive.fi/"
	var client http.Client
	rgb_result, ok := http_get(client, url)
	if !ok {
		log.Fatal("Failed to request rgb")
	}
	id := C.int(0)
	hexa_url := fmt.Sprintf(
		"https://chall03.hive.fi/?id=%d&resp=%s",
		id,
		C.GoString(C.body_to_hex(C.CString(rgb_result), &id)),
	)
	hexa_result, ok := http_get(client, hexa_url)
	if !ok {
		log.Fatal("Failed to request hexa")
	}
	log.Println(hexa_result)
}
