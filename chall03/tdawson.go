package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"time"
)

func execTime(start time.Time) {
	fmt.Printf("Finished in %dms\n", time.Since(start).Milliseconds())
}

func httpGet(url string) string {
	fmt.Printf("GET:\t%s\n", url)
	res, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("STATUS: %d %s\n", res.StatusCode, http.StatusText(res.StatusCode))

	body, err := ioutil.ReadAll(res.Body)
	res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("BODY:\t%s\n\n", string(body))
	return string(body)
}

func buildQuery(body string) string {
	var id, r, g, b int
	n, err := fmt.Sscanf(body, "id=%d,r=%d,g=%d,b=%d", &id, &r, &g, &b)
	if err != nil || n != 4 {
		log.Fatal(err)
	}
	return fmt.Sprintf("?id=%d&resp=%02x%02x%02x", id, r, g, b)
}

func main() {
	defer execTime(time.Now())
	url := "https://chall03.hive.fi/"
	query := buildQuery(httpGet(url))
	httpGet(url + query)
}
