package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func httpGet(url string) (bodyStr string) {
	res, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	body, err := ioutil.ReadAll(res.Body)
	res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(body))
	return string(body)
}

func parseBody(body string) (response string) {
	var id, r, g, b int
	n, err := fmt.Sscanf(body, "id=%d,r=%d,g=%d,b=%d - Send your response here: chall03.hive.fi/?id=<id>&resp=<hex>", &id, &r, &g, &b)
	if err != nil || n != 4 {
		log.Fatal(err)
	}
	response = fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%02x%02x%02x", id, r, g, b)
	fmt.Println(response)
	return response
}

func main() {
	url := "https://chall03.hive.fi/"
	response := parseBody(httpGet(url))
	httpGet(response)
}
