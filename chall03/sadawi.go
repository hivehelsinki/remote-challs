package main

import (
	"log"
	"net/http"
	"io/ioutil"
	"strings"
	"fmt"
	"strconv"
)

func main() {
	resp, err := http.Get("https://chall03.hive.fi/")
	if err != nil {
		log.Fatalln(err)
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(string(body))
	s := strings.Split(string(body), ",")
	id := s[0]
	r, _ := strconv.Atoi(strings.Split(s[1], "=")[1])
	g, _ := strconv.Atoi(strings.Split(s[2], "=")[1])
	b, _ := strconv.Atoi(strings.Split(strings.Split(s[3], " ")[0], "=")[1])
	rhex := fmt.Sprintf("%02x", r)
	ghex := fmt.Sprintf("%02x", g)
	bhex := fmt.Sprintf("%02x", b)
	log.Println(s)
	log.Println(id)
	log.Println(rhex)
	log.Println(ghex)
	log.Println(bhex)
	result :=  "https://chall03.hive.fi/?" + id + "&resp=" + rhex + ghex + bhex
	log.Println(result)
	resp1, err := http.Get(result)
	if err != nil {
		log.Fatalln(err)
	}
	body2, err := ioutil.ReadAll(resp1.Body)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(string(body2))
}
