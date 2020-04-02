package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"strings"
	"time"
)

var gTimeStart = time.Now()

func elapsedTime() time.Duration {
	return time.Since(gTimeStart) / 1e6
}

func makeGetRequest(url string) string {
	resp, err := http.Get(url)
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	defer resp.Body.Close()
	return string(body)
}

func generateHexRequestURL(url string, id string, respHex string) string {
	return url + "?id=" + id + "&resp=" + respHex
}

func main() {
	url := "https://chall03.hive.fi/"
	fmt.Printf("%dms - GET %s\n", elapsedTime(), url)

	body := makeGetRequest(url)
	fmt.Printf("%dms - GET %s\n", elapsedTime(), url)
	fmt.Printf("\tanswer:%s\n", body)

	s := strings.Split(body, "=")
	id := strings.Split(s[1], ",")[0]
	r, _ := strconv.Atoi(strings.Split(s[2], ",")[0])
	g, _ := strconv.Atoi(strings.Split(s[3], ",")[0])
	b, _ := strconv.Atoi(strings.Split(s[4], " ")[0])
	respHex := fmt.Sprintf("%02x%02x%02x", r, g, b)

	reqURL := generateHexRequestURL(url, id, respHex)

	fmt.Printf("%dms - GET %s\n", elapsedTime(), reqURL)
	body = makeGetRequest(reqURL)

	fmt.Printf("%dms - GET %s\n", elapsedTime(), reqURL)
	fmt.Printf("\tanswer: %s\n", body)
	fmt.Printf("%dms - DONE\n", elapsedTime())
}
