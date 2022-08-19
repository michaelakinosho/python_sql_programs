package main

import "fmt"

type Vertex struct {
	Lat, Long float64
	Name string
}

var m map[string]Vertex

func main() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967, "Home of C LANGUAGE",
	}
	fmt.Println(m)
	fmt.Printf("%v\n", m["Bell Labs"])
}