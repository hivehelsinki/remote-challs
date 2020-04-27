package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"regexp"
	"strconv"
	"strings"
)

var leadingInt = regexp.MustCompile(`^[-+]?\d+`)

func ParseLeadingInt(s string) (int64, error) {
	s = leadingInt.FindString(s)
	if s == "" {
		return 0, nil
	}
	return strconv.ParseInt(s, 10, 64)
}

func main() {
	resp, err := http.Get("https://chall03.hive.fi/")
	if err != nil {
		print(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		print(err)
	}
	s := strings.Split(fmt.Sprintf("%s", body), "=")
	id, err := ParseLeadingInt(s[1])
	ids := strconv.FormatInt(id, 10)
	red, err := ParseLeadingInt(s[2])
	green, err := ParseLeadingInt(s[3])
	blue, err := ParseLeadingInt(s[4])
	hexString := fmt.Sprintf("%x%x%x", red, green, blue)
	fmt.Print(string(body))
	resp.Body.Close()

	newURL := "https://chall03.hive.fi/?id=" + ids + "&resp=" + hexString
	resp2, err := http.Get(newURL)
	if err != nil {
		print(err)
	}
	defer resp2.Body.Close()
	body2, err := ioutil.ReadAll(resp2.Body)
	if err != nil {
		print(err)
	}
	fmt.Printf("\n")
	fmt.Print(string(body2))
	resp2.Body.Close()
}
