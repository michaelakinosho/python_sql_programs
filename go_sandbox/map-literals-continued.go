package main

import (
	"fmt"
)

type Vertex struct {
	Lat, Long float64
	Name string
}

var m = map[string]Vertex{
	"Bell Labs": {40.68433, -74.39967, "'Birth of C Language'"},
	"Google": {37.42202, -122.08408, "Googlplex"},
}

func main() {
	fmt.Println(m)
}