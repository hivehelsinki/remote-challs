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

func log_prefixed(msg string) {
	fmt.Printf("%d", time.Since(StartTime).Milliseconds())
	log.Println("ms - ", msg)
}

func get_request(address string) (id_rgb_str string) {
	log_prefixed("GET " + address)
	chall_req, err := http.Get(address)
	if err != nil {
		log.Fatal(err)
	}
	raw_id_rgb, err := ioutil.ReadAll(chall_req.Body)
	if err != nil {
		log.Fatal(err)
	}
	chall_req.Body.Close()
	id_rgb_str = fmt.Sprintf("%s", raw_id_rgb)
	log_prefixed("GET " + address + "\n\tanswer: " + id_rgb_str)
	return
}

func regexp_parse_before_slash(chall_body string) string {
	halved_string := strings.Split(chall_body, "-")
	reg, err := regexp.Compile("[^0-9=]+")
	if err != nil {
		log.Fatal(err)
	}
	return reg.ReplaceAllString(halved_string[0], "")
}

func extract_values(splitted []string) (id_value int, rgbs [3]int) {
	for i, element := range splitted {
		atoi_value, err := strconv.Atoi(element)
		if err != nil && i != 0 {
			log.Fatal(err)
		}
		if i == 1 {
			id_value = atoi_value
		} else if i > 1 {
			rgbs[i-2] = atoi_value
		}
	}
	return
}

func get_answer(ans_address string) {
	log_prefixed("GET " + ans_address)
	answer_req, err := http.Get(ans_address)
	if err != nil {
		log.Fatal(err)
	}
	parsed_answer, err := ioutil.ReadAll(answer_req.Body)
	if err != nil {
		log.Fatal(err)
	}
	answer_req.Body.Close()
	answer_str := fmt.Sprintf("%s", parsed_answer)
	log_prefixed("GET " + ans_address + "\n\tanswer: " + answer_str)
}

var StartTime = time.Now()

func main() {
	log.SetFlags(0)
	get_answer := get_request("https://chall03.hive.fi/")
	reqexp_values := regexp_parse_before_slash(get_answer)
	id_value, rgbs := extract_values(strings.Split(reqexp_values, "="))
	hex_string := fmt.Sprintf("%x%x%x", rgbs[0], rgbs[1], rgbs[2])
	ans_address := fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%s", id_value, hex_string)
	get_answer = get_request(ans_address)
	log_prefixed("DONE")
}
