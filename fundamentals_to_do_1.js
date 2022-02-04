// Setting and Swapping
// Set myNumber to 42
// Set myName to any name
var myNumber = 42
var myName = "Michael Akinosho"
console.log("my Number is:",myNumber)
console.log("my Name is:",myName)

// Now swap myNumber into myName & vice versa
temp = myNumber
myNumber = myName
myName = temp
console.log("my Number is:",myNumber)
console.log("my Name is:",myName)

var begin = 0
var end = 5

// Print -52 to 1066, using a FOR Loop
for (x = begin; x < end; x++) {
    console.log(x)
}

// Create beCheerful()
// Within it, console.log string "Good morning!"
// Call it x times,where x is a real number
function beCheerful() {
    console.log("Good morning")
}

i = 0
while ( i < end ) {
    beCheerful()
    i++
}

// Using FOR, print multiples of 3
// From -30 to 0. Skip -3 and -6
var begin = -30
var end = 0
for (x = begin; x <= end; x += 3) {
    if (x != -3 && x != -6){
        console.log("multiple of three is:",x)
    }
}

// Printing Integers with WHILE
i = 200
while (i <= 240) {
    console.log(i)
    i++
}

function myCheckBirthday(month,day) {
    if (month === 12 && day === 4){
        console.log("How did you know?")
    } else {
        console.log("Just another day...")
    }
}
myCheckBirthday(12,4)

function myCheckLeapYear(year) {
    var msg = "Year: " + year + " is NOT a Leap year"
    if (year%400 == 0) {
        msg = "Year: " + year + " is A Leap year"
    } else {
        if (year%100 != 0 && year%4 == 0) {
            msg = "Year: " + year + " is A Leap year"
        }
    }
    console.log(msg)
}
myCheckLeapYear(3000)

// Print all integer multiples of 5,
// from 512 to 4096.
// Afterward, also log how many there were
begin = 512
original_begin = begin
end = 4096
step = 5
counter = 0
if (begin <= end && step >= 1) {
    if (begin%step != 0) {
        begin += (step - begin%step)

    }
    for (x = begin; x <= end; x += step) {
        counter++
        console.log("Multiple:",counter,"between ",original_begin,"and",end,"is:",x)
        
    }
}

// Print multiples of 6 up to 60,000, using a WHILE
x = 0
step = 6
end = 60
while (x <= end) {
    console.log("Multiple of the number 6:",x)
    x += step
}

// Print integers 1 to 100.
// If divisible by 5, print "Coding" instead.
// If by 10, also print "Dojo"
begin = 1
end = 100
step = 1
for (x = begin; x <= end; x += step) {
    
    if (x%50 == 0) {
        console.log("Integer is:",x,"Coding Dojo Rocks!!!")
    } else if (x%10 == 0) {
        console.log("Integer is:",x,"Coding Dojo")
    } else if (x%5 == 0) {
        console.log("Integer is:",x,"Coding")
    } else {
        console.log("Integer is:",x)
    }
    
}

function myFunction(incoming="Expecting a message") {
    console.log(incoming)
}
myFunction("Happy to meet you!!")
myFunction()

// Add odd integers from -300000 to 300000
// Console.log the final sum. Is there a shortcut?
begin = -300000
original_begin = begin
end = 600000
step = 2
if (begin%2 == 0) {
    begin++
}
mySum = 0
for (x = begin; x <= end; x += step) {
    mySum += x
}
console.log("Sum of odd integers between",original_begin,"and",end,"is",mySum)

// Log positive numbers starting at 2016
// Counting down by fours (exclude 0), without a FOR loop
x = 2016
step = -4
while (x > 0) {
    console.log(x)
    x += step
}

// Based on earlier "Countdown by 4",
// Given lowNum, highNum, mult,
// Print multiples of mult from highNum down to lowNum
// Using a FOR
begin = 2 // lowNum
end = 9 // highNum
step = 3 // mult
original_end = end
counter = 0
if (begin <= end && step >= 1) {
    if (end%step != 0) {
        end -=  end%step
    }
    for (x = end; x >= begin; x -= step) {
        counter++
        console.log("Multiple:",counter,"between",begin,"and",original_end,"is:",x)
    }
}

// Given 4 parameters (param1, param2, param3, param4)
// Print the multiples of param1, starting at param2 and extending to param3
// One exception: if a multiple is equal to param4, then skip, do not print
begin = 5 // lowNum
original_begin = begin
end = 17 // highNum
step = 3 // mult this is param1
skip_mult = 9 // multiple to skip

if (begin <= end && step >= 1) {
    if (begin%step != 0) {
        begin += (step - begin%step)

    }
    console.log("Using a FOR Loop")
    counter = 0
    for (x = begin; x <= end; x += step) {
        counter++
        if (x != skip_mult) {
            console.log("Multiple:",counter,"of number",step,"between ",original_begin,"and",end,"is:",x)
        }
    }

    console.log("Using a WHILE Loop")
    counter = 0
    x  = begin
    while (x <= end) {
        counter++
        if (x != skip_mult) {
            console.log("Multiple:",counter,"of number",step,"between ",original_begin,"and",end,"is:",x)
        }
        x += step
    }
}