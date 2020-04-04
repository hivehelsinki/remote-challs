package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
  "strings"
  "strconv"
)

func main() {
  resp, err := http.Get("https://chall03.hive.fi/")
  if err != nil {
    return
  }
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {
    return
  }
  splitted := strings.Split(string(body), ",")

  red, err := strconv.Atoi(strings.Split(splitted[1], "=")[1])
  green, err := strconv.Atoi(strings.Split(splitted[2], "=")[1])
  blue, err := strconv.Atoi(strings.Split(strings.Split(splitted[3], "=")[1], " ")[0])
  hex := fmt.Sprintf("%02x%02x%02x", red, green, blue)
  id, err := strconv.Atoi(strings.Split(splitted[0], "=")[1])
  url := fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%s", id, hex)
  resp, err = http.Get(url)
  if err != nil {
    return
  }
  response, err := ioutil.ReadAll(resp.Body)
  if err != nil {
	  return
  }
  fmt.Printf("answer: %s (http status %d)\n", string(response), resp.StatusCode)
}
