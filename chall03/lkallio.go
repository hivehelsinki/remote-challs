 package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func retrieve_resp(address string) string {
	res, err := http.Get(address)
	if err != nil {
		log.Fatal(err)
	}
	out, err := ioutil.ReadAll(res.Body)
	res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}
	return string(out)
}

func get_values(a string) (int, int) {
	i := 0
	id := 0
	hex := 0
	meta_i := 0
	for meta_i < 4 {
		for a[i] < '0' || a[i] > '9' {
			i += 1
		}
		num := 0
		for !(a[i] < '0' || a[i] > '9') {
			num = num * 10 + int(a[i]) - '0'
			i += 1
		}
		if meta_i == 0 {
			id = num
		} else {
			hex = hex * 0x100 + num
		}
		meta_i += 1
	}
	return id, hex
}

func main() {
	id, hex := get_values(retrieve_resp("https://chall03.hive.fi"))
	id_string := fmt.Sprintf("%d", id)
	hex_string := fmt.Sprintf("%x", hex)
	fmt.Println(retrieve_resp("https://chall03.hive.fi/?id=" + id_string + "&resp=" + hex_string))
}