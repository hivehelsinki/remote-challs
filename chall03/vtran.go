package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	resp, err := http.Get("https://chall03.hive.fi/")
	ifError(err)
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := ioutil.ReadAll(resp.Body)
		ifError(err)

		s := parseStringToQuerry(string(bodyBytes))
		res, err := http.Get(s)
		ifError(err)

		defer res.Body.Close()
		println(res.StatusCode)
	}
}

func parseStringToQuerry(str string) string {
	var id, r, g, b int
	fmt.Sscanf(str, "id=%d,r=%d,g=%d,b=%d", &id, &r, &g, &b)
	return fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%02x%02x%02x", id, r, g, b)
}

func ifError(err error) {
	if err != nil {
		log.Fatalln(err)
	}
}
