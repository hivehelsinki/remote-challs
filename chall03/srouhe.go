package main

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
	"net/http"
	"io/ioutil"
)


func errCheck(err error) {
	if err != nil {
        log.Fatalf("Fatal error: %v", err)
    }
}

func parseResp(respBody string) (string) {

	re, err := regexp.Compile("id=(\\d*).*r=(\\d{1,3}).*g=(\\d{1,3}).*b=(\\d{1,3})")
	errCheck(err)
	matches := re.FindAllStringSubmatch(respBody, -1)
	r, err := strconv.Atoi(matches[0][2])
	errCheck(err)
	g, err := strconv.Atoi(matches[0][3])
	errCheck(err)
	b, err := strconv.Atoi(matches[0][4])
	errCheck(err)
	return (fmt.Sprintf("https://chall03.hive.fi/?id=%v&resp=%.2x%.2x%.2x", matches[0][1], r, g, b))
}

func main() {
	resp, err := http.Get("https://chall03.hive.fi/")
	defer resp.Body.Close()
	errCheck(err)

	body, err := ioutil.ReadAll(resp.Body)
	errCheck(err)

	response, err := http.Get(parseResp(string(body)))
	defer response.Body.Close()
	errCheck(err)
	log.Printf("Response status code: [%v]\n", response.StatusCode)
}
