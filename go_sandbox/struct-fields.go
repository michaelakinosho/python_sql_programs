package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{5, 2}
	v.X = 3
	fmt.Println("value of X in vertex is:", v.X)
	fmt.Printf("value of Y in vertex is: %v\n", v.Y)
	fmt.Println(v)
}