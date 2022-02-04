// Given an array and an additional value
// Insert this value at the beginning of the array
// Do this without using any built-in array methods
function pushFront(arr = [12,23,34], val = 1) {
    
    len = arr.length
    temp = [val]
    i = 0
    while (i < len) {
        temp[i+1] = arr[i]
        i++
    }
    arr = temp
    console.log("New array is:",arr)
    return arr
}
pushFront()

// Given an array remove and return the value at the beginning of the array.
// Do this without using any built-in array methods
function popFront(arr = [12,23,34]) {
    len = arr.length
    temp = []
    i = 0
    var val = arr[i]
    i++
    while (i < len) {
        temp[i-1] = arr[i]
        i++
    }
    arr = temp
    console.log("First value is:",val)
    console.log("New array is:",arr)
    return arr, val
}
popFront()

// Given an array, index, and additional value,
// Insert the value into array at given index.
// Do this without built-in array methods
function insertAt(arr = [12,23,34],idx=1,val=99) {
    len = arr.length
    temp = []
    i = 0
    while (i < len) {
        if (i != idx) {
            temp[i] = arr[i]
        } else {
            temp[i] = val
        }
        i++
    }
    arr = temp
    console.log("New array is:",arr)
    return arr
}
insertAt()

// Adding my own case, so array by value added at index position
// For example arr = [12,23,34], index = 1, value = 99
// New arr = [12,99,23,34]
function addAt(arr = [12,23,34],idx=1,val=99) {
    len = arr.length
    temp = []
    i = 0
    j = 0
    while (i < len) {
        if (i != idx) {
            temp[j] = arr[i]
        } else if (i == idx) {
            temp[j] = val
            j++
            temp[j] = arr[i]
        }
        i++
        j++
    }
    arr = temp
    console.log("New array is:",arr)
    return arr
}
addAt()

// Given an array and an index into array,
// remove and return the array value at that index
// Do this without using built-in array methods
function removeAt(arr = [12,23,34], idx = 1) {
    len = arr.length
    temp = []
    i = 0
    j = 0
    while (i < len) {
        if (i != idx) {
            temp[j] = arr[i]
        } else if (i == idx) {
            var val = arr[i]
            j--
        }
        i++
        j++
    }
    arr = temp
    console.log("Removed value is:",val)
    console.log("New array is:",arr)
}
removeAt()

// Swap positions of successive pairs of values of given array.
// If length is odd, do not change the final element.
function swapPairs(arr = [12,23,34,45]) {
    len = arr.length
    if (len%2 == 1) {
        len--
    }
    temp = []
    i = 0
    while (i < len) {
        first = arr[i]
        second = arr[i+1]
        arr[i] = second
        arr[i+1] = first
        i = i + 2
    }
    console.log(arr)
}
swapPairs()

// Sara is looking to hire an awesome web developer and has received applications from various sources.
// Her assistant alphabetized them but noticed some duplicates.
// Given a sorted array, remove duplicate values.
// Because array elements are already in order, all duplicate values will be grouped together.
// As with all these array challenges, do this without using any built-in array methods
function removeDuplicates(arr = [1,1,1,1,2,2,3,3,3,3,3,3,4,4,5,5,5,5,5,5,5,5]) {
    len = arr.length
    temp = []
    i = 0
    temp[0] = arr[i]
    i++
    while (i < len) {
        temp_len = temp.length
        if (temp[temp_len-1] != arr[i]) {
            temp[temp_len] = arr[i]
        }
        i++
    }
    console.log(temp)
}
removeDuplicates()