package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := 1.0
	if math.Pow(z, 2) == x {
		fmt.Printf("Found square root of %v: %v\n", x, z)
	} else if x <= 0 {
		fmt.Printf("Unable to determine square root of %v\n", x)
	} else {
		temp_z := z * -1
		i := 1
		for math.Pow(z, 2) != x {
			if i > 100 || z == temp_z {
				break
			}
			temp_z = z
			z -= (z*z - x) / (2 * z)
			if math.Pow(z, 2) == x {
				fmt.Printf("Found square root of %v: %v\n", x, z)
			}
			fmt.Printf("Value of z^2: %v, Value of z: %v, value of temp_z: %v, value of i: %v\n", math.Pow(z, 2), z, temp_z, i)
			i++
		}
	}
	return 0
}

func main() {
	fmt.Println(Sqrt(3.14578))
}
