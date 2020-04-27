package main

import(
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"regexp"
	"strconv"
	"time"
)

func main(){
	start := time.Now()
	resp, err := http.Get("https://chall03.hive.fi/")
	if err != nil {
		log.Fatalln(err)
	}
	body, err := ioutil.ReadAll(resp.Body)
	defer resp.Body.Close()
	if err != nil{
		log.Fatalln(err)
	}
	fmt.Println("GET	https://chall03.hive.fi/")
	fmt.Printf("	answer: %s\n\n", string(body))

	r := regexp.MustCompile(`\d+`)
	matches := r.FindAllString(string(body), -1)

	id, err := strconv.Atoi(matches[0])
	red, err := strconv.Atoi(matches[1])
	green, err := strconv.Atoi(matches[2])
	blue, err := strconv.Atoi(matches[3])

	hex := fmt.Sprintf("%02x%02x%02x", red, green, blue)
	url := fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%s", id, hex)
	fmt.Printf("GET	%s\n",url)

	resp2, err := http.Get(url)
	if err != nil {
		log.Fatalln(err)
	}
	body1, err := ioutil.ReadAll(resp2.Body)
	defer resp2.Body.Close()
	if err != nil{
		log.Fatalln(err)
	}
	
	fmt.Printf("	answer: %s\n", string(body1))
	fmt.Printf("	status code: %d\n\n", resp2.StatusCode)
	
	elapsed := time.Since(start).Milliseconds()
    log.Printf("Only took %d ms", elapsed)
}
