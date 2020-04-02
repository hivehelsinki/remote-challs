package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

func mySplit(r rune) bool {
	return r == '=' || r == ','
}

func myErrorCheck(err error) {
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}
}

func myGetResponse(str string) string {
	resp, err := http.Get(str)
	myErrorCheck(err)
	content, err := ioutil.ReadAll(resp.Body)
	defer resp.Body.Close()
	myErrorCheck(err)
	return string(content)
}

func myConvertToHex(color string) string {
	nb, err := strconv.Atoi(color)
	myErrorCheck(err)
	hex := strconv.FormatInt(int64(nb), 16)
	if len(hex) == 1 {
		return "0" + hex
	}
	return hex
}

func myColorConverter(r, g, b string) string {
	return (string(myConvertToHex(r)) +
		string(myConvertToHex(g)) +
		string(myConvertToHex(b)))
}

func main() {
	started := time.Now()

	url := "https://chall03.hive.fi/"
	content := myGetResponse(url)
	fmt.Println("answer: " + content)

	// Split string with " " to get value part and response url
	parts := strings.Split(string(content), " ")
	// Split value part with "=" or "," to get values
	subparts := strings.FieldsFunc(parts[0], mySplit)
	// Convert RGB values to hex, trying without printf
	strhex := myColorConverter(subparts[3], subparts[5], subparts[7])
	// Replace id and hex from response url
	r := strings.NewReplacer("<id>", subparts[1], "<hex>", strhex)
	newurl := r.Replace(parts[6])

	content = myGetResponse("https://" + newurl)
	fmt.Println("answer: " + content)

	fmt.Printf("DONE: %dms\n", time.Since(started).Milliseconds())
}
