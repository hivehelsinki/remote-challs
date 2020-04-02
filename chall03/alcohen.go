package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
	"time"
	"strings"
	"strconv"
	"log"
)

func make_get_request(url string) string {
	resp, err := http.Get(url)
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	defer resp.Body.Close()
	return string(body)
}

func generate_hex_request_url(url string, id string, resp_hex string) string {
	return url + "?id=" + id + "&resp=" + resp_hex
}

func main() {
	start := time.Now()
	url := "https://chall03.hive.fi/"
	elapsed := time.Since(start) / 1e6
	fmt.Printf("%dms - GET %s\n", elapsed, url)
	
	body := make_get_request(url)
	elapsed = time.Since(start) / 1e6
	fmt.Printf("%dms - GET %s\n", elapsed, url)
	fmt.Printf("\tanswer:%s\n", body)
	
	s := strings.Split(body, "=")
	
	//id, r, g, b := s[1], s[2], s[5], s[4]
	//id, _ := strconv.Atoi(strings.Split(s[1], ",")[0])
	id := strings.Split(s[1], ",")[0]
	r, _ := strconv.Atoi(strings.Split(s[2], ",")[0])
	g, _ := strconv.Atoi(strings.Split(s[3], ",")[0])
	b, _ := strconv.Atoi(strings.Split(s[4], " ")[0])
	resp_hex := fmt.Sprintf("%02x%02x%02x", r, g, b)

	req_url := generate_hex_request_url(url, id, resp_hex)
	fmt.Printf("%dms - GET %s\n", elapsed, req_url)
	body = make_get_request(req_url)
	elapsed = time.Since(start) / 1e6
	fmt.Printf("%dms - GET %s\n", elapsed, req_url)
	fmt.Printf("\tanswer: %s\n", body)
	fmt.Printf("%dms - DONE\n", elapsed)
}
