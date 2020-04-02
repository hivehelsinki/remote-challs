package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func httpGet() {
	res, err := http.Get("https://chall03.hive.fi")
	if err != nil {
		log.Fatal(err)
	}
	body, err := ioutil.ReadAll(res.Body)
	res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}

	var id, r, g, b int
	n, err := fmt.Sscanf(string(body), "id=%d,r=%d,g=%d,b=%d - Send your response here: chall03.hive.fi/?id=<id>&resp=<hex>", &id, &r, &g, &b)
	if err != nil || n != 4 {
		log.Fatal(err)
	}
	response := fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%02x%02x%02x", id, r, g, b)
	fmt.Println(response)
	res, err = http.Get(response)
	if err != nil {
		log.Fatal(err)
	}
	body, err = ioutil.ReadAll(res.Body)
	res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(body))
}

func main() {
	httpGet()
}
