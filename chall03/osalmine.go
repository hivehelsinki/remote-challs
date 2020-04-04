package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"log"
	"strings"
	"strconv"
)

func get_rgb_id (s string) (int, int, int, int) {
	str := strings.Split(s, " ")
	vals := strings.Split(str[0], ",")
	id, err := strconv.Atoi(strings.Split(vals[0], "=")[1]);
	r, err := strconv.Atoi(strings.Split(vals[1], "=")[1]);
	g, err := strconv.Atoi(strings.Split(vals[2], "=")[1]);
	b, err := strconv.Atoi(strings.Split(vals[3], "=")[1]);
	if err != nil {
		log.Fatal(err)
	}
	return id, r, g, b
}

func main() {
	url := "https://chall03.hive.fi/"
	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	s := fmt.Sprintf("%s", body)
	id, r, g, b := get_rgb_id(s)
	fmt.Printf("id: %d, r: %d g: %d, b: %d\n", id, r, g, b)
	response := fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%02x%02x%02x", id, r, g, b)
	fmt.Println(response)
	resp, err = http.Get(response);
	if err != nil {
		log.Fatal(err)
	}
	body, err = ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(body))
}
