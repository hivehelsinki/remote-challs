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

func get_values(content string) (int, int) {
	id := 0
	hex := 0
	loop_phase := 0
	i := 0
	for loop_phase < 4 {
		for content[i] < '0' || content[i] > '9' {
			i += 1
		}
		num := 0
		for !(content[i] < '0' || content[i] > '9') {
			num = num * 10 + int(content[i]) - '0'
			i += 1
		}
		if loop_phase == 0 {
			id = num
		} else {
			hex = hex * 0x100 + num
		}
		loop_phase += 1
	}
	return id, hex
}

func main() {
	id, hex := get_values(retrieve_resp("https://chall03.hive.fi"))
	id_string := fmt.Sprintf("%d", id)
	hex_string := fmt.Sprintf("%x", hex)
	fmt.Println(retrieve_resp("https://chall03.hive.fi/?id=" + id_string + "&resp=" + hex_string))
}