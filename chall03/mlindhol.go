package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func error() {
	fmt.Printf("whoops, error!\n")
	os.Exit(1)
}

func main() {

	resp, err := http.Get("https://chall03.hive.fi/")
	if err != nil {
		error()
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		error()
	}

	str := strings.Split(string(body), ",")

	reg, err := regexp.Compile("[^0-9]+")
	if err != nil {
		error()
	}

	id, err := strconv.Atoi(reg.ReplaceAllString(str[0], ""))
	r, err := strconv.Atoi(reg.ReplaceAllString(str[1], ""))
	g, err := strconv.Atoi(reg.ReplaceAllString(str[2], ""))
	b, err := strconv.Atoi(strings.TrimSuffix(reg.ReplaceAllString(str[3], ""), "03"))
	if err != nil {
		error()
	}

	hex := fmt.Sprintf("%02x%02x%02x", r, g, b)
	resp, err = http.Get(fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%s", id, hex))
	if err != nil {
		error()
	}
	response, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		error()
	}
	fmt.Printf("answer: %s\n[status code %d]\n", string(response), resp.StatusCode)
}
