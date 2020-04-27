package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func httpGet(url string) string {
	result, err := http.Get(url)
	if err != nil {
		log.Fatalln(err)
	}
	content, err := ioutil.ReadAll(result.Body)
	if err != nil {
		log.Fatalln(err)
	}
	result.Body.Close()
	fmt.Println(string(content))
	return (string(content))
}

func respondToURL(content string) {
	var id, r, g, b int

	getInfo, err := fmt.Sscanf(string(content), "id=%d,r=%d,g=%d,b=%d - Send your response here: chall03.hive.fi/?id=<id>&resp=<hex>", &id, &r, &g, &b)
	if err != nil || getInfo != 4 {
		log.Fatalln(err)
	}
	res := fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%02x%02x%02x", id, r, g, b)
	respond, err := http.Get(res)
	if err != nil {
		log.Fatalln(err)
	}
	cont, err := ioutil.ReadAll(respond.Body)
	if err != nil {
		log.Fatalln(err)
	}
	respond.Body.Close()
	fmt.Printf("respond: " + string(cont))
}

func main() {
	url := "https://chall03.hive.fi/"
	content := httpGet(url)
	respondToURL(content)
}
