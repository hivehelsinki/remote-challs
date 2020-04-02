package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"strings"
)

func main() {
	client := http.Client{}
	res, err := client.Get("https://chall03.hive.fi")
	if err != nil {
		log.Fatal(err)
	}
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(body))
	id := string(body)[0:strings.Index(string(body), ",")]
	rgb := string(body)[strings.Index(string(body), ",")+1 : strings.Index(string(body), " ")]
	rgb_separated := strings.Split(rgb, ",")
	r, _ := strconv.Atoi(rgb_separated[0][2:])
	g, _ := strconv.Atoi(rgb_separated[1][2:])
	b, _ := strconv.Atoi(rgb_separated[2][2:])
	hex := fmt.Sprintf("%02x%02x%02x", r, g, b)
	res, err = client.Get("https://chall03.hive.fi/?" + id + "&resp=" + hex)
	if err != nil {
		log.Fatal(err)
	}
	body, err = ioutil.ReadAll(res.Body)
	fmt.Println(string(body))
}
