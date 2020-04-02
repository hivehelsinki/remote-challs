package main

import (
	"fmt"
	"net/http"
	"strings"
	"strconv"
	"io/ioutil"
)

func	getData(addr string) string {
	fmt.Println(addr)
	response, err := http.Get(addr)
	if err != nil {
		return ("error")
	}
	print(string(response.StatusCode) + response.Status + "\n")
	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		return ("error")
	}
	responseString := string(responseData)
	fmt.Println("answer: " + responseString)
	return responseString
}

func	sendResponse(response string, addr string) int {
	values_str := strings.Split(response, " ")[0]
	values := strings.Split(values_str, ",")
	r, _ := strconv.Atoi(strings.Split(values[1], "=")[1])
	g, _ := strconv.Atoi(strings.Split(values[2], "=")[1])
	b, _ := strconv.Atoi(strings.Split(values[3], "=")[1])
	hex := fmt.Sprintf("%02x%02x%02x", r, g, b)
	response = getData(addr + "?" + values[0] + "&resp=" + hex)
	if (response == "error") {
		return (0)
	}
	return (1)
}

func main() {
	addr := "https://chall03.hive.fi/"

	response := getData(addr)
	fmt.Println("")
	if (response == "error" || sendResponse(response, addr) == 0) {
		fmt.Println("error")
	}
	return
}
