package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"strings"
)

func parseResponse(response string) (map[string]int, string) {
	splitted := strings.Split(response, "-")
	values := strings.Split(strings.Trim(splitted[0], " "), ",")
	valuemap := make(map[string]int)
	var id string = ""
	for _, value := range values {
		elem := strings.Split(value, "=")
		if elem[0] == "id" {
			id = elem[1]
		} else {
			valuemap[elem[0]], _ = strconv.Atoi(elem[1])
		}
	}
	return valuemap, id
}

func validColors(values map[string]int) bool {
	for _, value := range values {
		if value > 255 || value < 0 {
			return false
		}
	}
	return true
}

func convertHex(values map[string]int) (string, error) {
	if !validColors(values) {
		return "", errors.New("invalid rgb values")
	}
	hex := fmt.Sprintf("%02x%02x%02x", values["r"], values["g"], values["b"])
	return hex, nil
}

func httpGet(url string) (string, error) {
	response, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
		return "", err
	}
	data, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Fatal(err)
		return "", err
	}
	response.Body.Close()
	return string(data), nil
}

func main() {
	var baseURL string = "https://chall03.hive.fi/"
	body, err := httpGet(baseURL)
	if err != nil {
		return
	}
	values, id := parseResponse(body)
	hex, err := convertHex(values)
	if err != nil {
		log.Fatal(err)
		return
	}
	body, err = httpGet(baseURL + "?id=" + id + "&resp=" + hex)
	if err != nil {
		return
	}
	fmt.Println(body)
}
