package main

import "fmt"

type Vertex struct {
	X, Y int
}

var (
	v1 = Vertex{1, 2}
	v2 = Vertex{X: 1}	// Y:0 is implicit
	v3 = Vertex{}
	p = &Vertex{1, 2}
)

func main() {
	fmt.Println(v1, p.X, v2, v3)
}