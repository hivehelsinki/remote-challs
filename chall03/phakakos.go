package main


import (
	"net/http"
	"io/ioutil"
	"fmt"
	"log"
	"strconv"
	"time"
)

func hexaConv(num int) string {
	a, b := '0', '0'
	y, u := 0, 0
	var ret string
	u = num % 16
	y = num / 16
	if (u > 9){
		b = rune('a' + u - 10)
	} else {
		b = rune('0' + u)
	}
	if (y > 9){
		a = rune('a' + y - 10)
	} else {
		a = rune('0' + y)
	}
	ret = string(a) + string(b)
	//ret = append(ret, b)
	return ret
}


func main() {
	start := time.Now()
	fmt.Printf("Making the request\n")
	resp, err := http.Get("https://chall03.hive.fi/")
	if err != nil {
    log.Fatal(err)
    }
	defer resp.Body.Close()
	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			log.Fatal(err)
		}
		bodyString := string(bodyBytes)
		//t := time.Now()
		fmt.Printf("%d MS | %s\n", time.Now().Sub(start).Milliseconds(), bodyString)
		i, id, red, green, blue, valNum, reading := 0, 0, 0, 0, 0, 0, 0
		for valNum != 4 {
			if (bodyString[i] == '='){
				reading = 1
			} else if (bodyString[i] == ',' || bodyString[i] == ' '){
				reading = 0
				valNum++
			}else{
				if (reading == 1 && valNum == 0){
					if (id > 0){
						id = id * 10
						}
					id += int(bodyString[i] - '0')
				}
				
				if (reading == 1 && valNum == 1){
					if (red > 0){
						red = red * 10
						}
					red += int(bodyString[i] - '0')
				}
				
				if (reading == 1 && valNum == 2){
					if (green > 0){
						green = green * 10
						}
					green += int(bodyString[i] - '0')
				}
				
				if (reading == 1 && valNum == 3){
					if (blue > 0){
						blue = blue * 10
						}
					blue += int(bodyString[i] - '0')
				}
			}
			i++
		}
		fmt.Printf("%d MS | id %d red %d green %d blue %d\n", time.Now().Sub(start).Milliseconds(), id, red, green, blue)
		
		cRed, cGreen, cBlue := hexaConv(red), hexaConv(green), hexaConv(blue)
		fColor := cRed + cGreen + cBlue
		fmt.Printf("%d MS | color: %s\n", time.Now().Sub(start).Milliseconds(), fColor)
		fGetAdd := "https://chall03.hive.fi/?id=" + strconv.FormatInt(int64(id), 10) + "&resp=" + fColor

		fmt.Printf("%d MS | second GET to %s\n", time.Now().Sub(start).Milliseconds(), fGetAdd)
		respo, err := http.Get(fGetAdd)
		if err != nil {
			log.Fatal(err)
		}
		defer respo.Body.Close()
		if respo.StatusCode == http.StatusOK {
			fbodyBytes, err := ioutil.ReadAll(respo.Body)
			if err != nil {
				log.Fatal(err)
			}
			bodyString2 := string(fbodyBytes)
			fmt.Printf("%d MS | Response %d\n%s", time.Now().Sub(start).Milliseconds(), respo.StatusCode, bodyString2)
		} else {
			fmt.Printf("%d MS | Response %d", time.Now().Sub(start).Milliseconds(), respo.StatusCode)
		}
	}
}