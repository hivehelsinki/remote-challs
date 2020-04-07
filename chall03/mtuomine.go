package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"regexp"
	"strconv"
	"strings"
	"time"
)

const baseURL = "https://chall03.hive.fi/"

func main() {
	client := http.Client{Timeout: time.Second * 1}

	// First request
	res, err := client.Get(baseURL)
	checkErr(err)

	body, err := ioutil.ReadAll(res.Body)
	checkErr(err)
	res.Body.Close()

	// Second request
	res, err = client.Get(baseURL + createQuery(string(body)))
	checkErr(err)
	defer res.Body.Close()
	fmt.Println(res.StatusCode)
}

func checkErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func parseNumbers(str string) []string {
	re := regexp.MustCompile("[0-9]+")
	arr := re.FindAllString(strings.Split(str, "-")[0], -1)
	if len(arr) != 4 {
		log.Fatal("Unexpected string...")
	}
	return arr
}

func createQuery(answer string) string {
	values := parseNumbers(answer)
	r, err := strconv.Atoi(values[1])
	checkErr(err)
	g, err := strconv.Atoi(values[2])
	checkErr(err)
	b, err := strconv.Atoi(values[3])
	checkErr(err)
	str := fmt.Sprintf("?id=%s&resp=%02x%02x%02x", values[0], r, g, b)
	return str
}
