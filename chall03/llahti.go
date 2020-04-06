package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"strings"
)

func getRgb(str string, start int, end int) string {
	color, err := strconv.Atoi(str[start:end])
	if err != nil {
		log.Fatalln(err)
	}
	return fmt.Sprintf("%.2x", color)
}

func getHTTPResponse(address string) string {
	resp, err := http.Get(address)
	if err != nil {
		log.Fatalln(err)
	}

	defer resp.Body.Close()

	response, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}

	return string(response)
}

func main() {
	str := getHTTPResponse("https://chall03.hive.fi/")

	idIndex := strings.Index(str, "id=") + 3
	rIndex := strings.Index(str, "r=") + 2
	gIndex := strings.Index(str, "g=") + 2
	bIndex := strings.Index(str, "b=") + 2
	bEnd := strings.Index(str, " - ")

	id := str[idIndex : rIndex-3]
	r := getRgb(str, rIndex, gIndex-3)
	g := getRgb(str, gIndex, bIndex-3)
	b := getRgb(str, bIndex, bEnd)

	arr := []string{"https://chall03.hive.fi/?id=", id, "&resp=", r, g, b}
	address := strings.Join(arr, "")

	fmt.Printf(getHTTPResponse(address))
}
