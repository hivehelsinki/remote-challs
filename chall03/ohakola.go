package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func parse_rgb_response_into_url(body string) string {
	var id, r, g, b int
	parser, err := fmt.Sscanf(
		string(body),
		"id=%d,r=%d,g=%d,b=%d - Send your response here: chall03.hive.fi/?id=<id>&resp=<hex>",
		&id,
		&r,
		&g,
		&b,
	)
	if parser != 4 || err != nil {
		log.Fatal(err)
	}
	return fmt.Sprintf(
		"https://chall03.hive.fi/?id=%d&resp=%s",
		id,
		fmt.Sprintf("%02x%02x%02x", r, g, b),
	)
}

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
	hexa_url := parse_rgb_response_into_url(rgb_result)
	hexa_result, ok := http_get(client, hexa_url)
	if !ok {
		log.Fatal("Failed to request hexa")
	}
	log.Println(hexa_result)
}
