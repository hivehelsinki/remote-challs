package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func httpGet() {
	res, err := http.Get("https://chall03.hive.fi")
	if err != nil {
		fmt.Printf("ERROR\n")
	}
	body, err := ioutil.ReadAll(res.Body)
	defer res.Body.Close()

	if err != nil {
		fmt.Printf("ERROR\n")
	}

	fmt.Println(string(body))
	var id int
	var r int
	var g int
	var b int
	n, err := fmt.Sscanf(string(body), "id=%d,r=%d,g=%d,b=%d - Send your response here: chall03.hive.fi/?id=<id>&resp=<hex>", &id, &r, &g, &b)
	if err != nil || n != 4 {
		fmt.Printf("ERROR\n")
	}
	fmt.Printf("id:%d r:%d g:%d b:%d\n", id, r, g, b)
	response := fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%02x%02x%02x", id, r, g, b)
	fmt.Println(response)
	res, err = http.Get(response)
	if err != nil {
		fmt.Printf("ERROR\n")
	}
	defer res.Body.Close()
	body, err = ioutil.ReadAll(res.Body)
	fmt.Println(string(body))
}

func main() {
	httpGet()
}
