package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strconv"
	"strings"
)

func convertRGBToHex(rs, gs, bs string) string {
	r, err := strconv.Atoi(rs)
	if err != nil {
		fmt.Println(err)
	}
	g, err := strconv.Atoi(gs)
	if err != nil {
		fmt.Println(err)
	}
	b, err := strconv.Atoi(bs)
	if err != nil {
		fmt.Println(err)
	}
	result := fmt.Sprintf("%x%x%x", r, g, b)
	return result
}

func main() {
	getResponse, err := http.Get("https://chall03.hive.fi/")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer getResponse.Body.Close()
	getBody, err := ioutil.ReadAll(getResponse.Body)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	bd := strings.Split(string(getBody), " ")[0]
	d := strings.Split(bd, ",")
	id := strings.Split(d[0], "=")[1]
	r := strings.Split(d[1], "=")[1]
	g := strings.Split(d[2], "=")[1]
	b := strings.Split(d[3], "=")[1]
	hex := convertRGBToHex(r, g, b)

	req, err := http.NewRequest("POST", "https://chall03.hive.fi", nil)
	q := req.URL.Query()
	q.Add("id", id)
	q.Add("resp", hex)
	req.URL.RawQuery = q.Encode()

	postResponse, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer postResponse.Body.Close()

	postbody, err := ioutil.ReadAll(postResponse.Body)
	fmt.Println(string(postbody))
}
