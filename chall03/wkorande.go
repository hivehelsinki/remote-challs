package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"
	"strings"
)

func convertRGB(rs, gs, bs string) string {
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
	resp, err := http.Get("https://chall03.hive.fi/")
	if err != nil {
		fmt.Println(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
	}
	bd := strings.Split(string(body), " ")[0]
	d := strings.Split(bd, ",")

	id := strings.Split(d[0], "=")[1]
	r := strings.Split(d[1], "=")[1]
	g := strings.Split(d[2], "=")[1]
	b := strings.Split(d[3], "=")[1]
	hex := convertRGB(r, g, b)

	presp, err := http.Post("https://chall03.hive.fi/?id="+id+"&resp="+hex, "", nil)
	if err != nil {
		fmt.Println(err)
	}
	postbody, err := ioutil.ReadAll(presp.Body)
	fmt.Println(string(postbody))
}
