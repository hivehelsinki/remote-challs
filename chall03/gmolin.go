package main

import (
	"net/http"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func http_post_hex(id string, hex string)string{
	result, err := http.Get("https://chall03.hive.fi/?id="+id+"&resp="+hex)
	if err != nil {
		fmt.Println(err)
	}
	body, err := ioutil.ReadAll(result.Body)
	return string(body)
}

func http_get_id_rgb(www string)[]string{
	result, err := http.Get(www)
	if err != nil {
		fmt.Println(err)
	}
	body, err := ioutil.ReadAll(result.Body)
	if err != nil{
		fmt.Println(err)
	}
	sliced_body := strings.Split(string(body), ",")
	return sliced_body
}

func main(){
	sliced_body := http_get_id_rgb("https://chall03.hive.fi/")
	fmt.Println(sliced_body)
	id_array := strings.Split(sliced_body[0], "=")
	r_array := strings.Split(sliced_body[1], "=")
	g_array := strings.Split(sliced_body[2], "=")
	b_array_all := strings.Split(sliced_body[3], "=")
	b_array_only_b := strings.Split(b_array_all[1], " ")
	id := id_array[1]
	r, _ := strconv.Atoi(r_array[1])
	g, _ := strconv.Atoi(g_array[1])
	b, _ := strconv.Atoi(b_array_only_b[0])
	hex := fmt.Sprintf("%02x%02x%02x", r, g, b)
	body := http_post_hex(id, hex)
	fmt.Println(body)
}
