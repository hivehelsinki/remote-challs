package main

import (
    "fmt"
    "time"
    "io/ioutil"
    "log"
    "net/http" 
    "strings"
    "strconv"
    )

func main() {
// Time stampe 00
    start := time.Now()
    fmt.Println(": 000.0000 ms")

// Get Request from URL
    resp, err := http.Get("https://chall03.hive.fi/")
    if err != nil {
        log.Fatalln(err)
    }
	body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        log.Fatalln(err)
    }
    fmt.Println(string(body))

// Time stampe 01
    elapsed1 := time.Since(start)
    fmt.Println(":", elapsed1)

// Convert string and get color in Hex. 
    split :=strings.Split(string(body), " ")
    splitted := strings.Split(string(split[0]), ",")
    id, err := strconv.Atoi(strings.Split(splitted[0], "=")[1])
    red, err := strconv.Atoi(strings.Split(splitted[1], "=")[1])
    green, err := strconv.Atoi(strings.Split(splitted[2], "=")[1])
    blue, err := strconv.Atoi(strings.Split(splitted[3], "=")[1])
    hex := fmt.Sprintf("%02x%02x%02x", red, green, blue)  
    url := fmt.Sprintf("https://chall03.hive.fi/?id=%d&resp=%s", id, hex)

// Requst from URL again
    resp, err = http.Get(url)
    if err != nil {
        log.Fatalln(err)
    }
    response, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        log.Fatalln(err)
    }
    fmt.Printf("answer: %s\n", response)

// Time stampe 02
    elapsed2 := time.Since(start)
    fmt.Println(":", elapsed2)
}



