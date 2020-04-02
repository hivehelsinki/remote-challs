package main

import (
	"io/ioutil"
	"fmt"
	"strings"
	"net/http"
	"strconv"
)

func main() {
	res, err := http.Get("https://chall03.hive.fi/")
	body, err := ioutil.ReadAll(res.Body)
	tmp := strings.Split(string(body), " ")
	str := strings.Split(tmp[0], ",")
	id, err := strconv.Atoi(str[0][3:len(str[0])])
	r, err := strconv.Atoi(str[1][2:len(str[1])])
	g, err := strconv.Atoi(str[2][2:len(str[2])])
	b, err := strconv.Atoi(str[3][2:len(str[3])])
	var rgb string = fmt.Sprintf("%02x%02x%02x", r, g, b);
	var url string = "https://chall03.hive.fi/?id=" + strconv.Itoa(id) + "&resp=" + rgb
	res2, err := http.Get(url)
	body2, err := ioutil.ReadAll(res2.Body)
	fmt.Println(string(body2))
	_ = err;
}
