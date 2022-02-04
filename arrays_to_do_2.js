// Given a numerical array, reverse the order of values, in-place.
// The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed.
// Working 'in-place' means that you cannot use a second array - move values within the array that you are given.
// As always, do not use built-in array functions such as splice()
function reverseArr(arr = [11,22,33,44,55,66,77,88,99]) {
    len = arr.length
    half_len = Math.floor(len/2)
    console.log(arr)
    i = 0
    while (i < half_len) {
        first = arr[i]
        last = arr[len-i-1]
        arr[i] = last
        arr[len-i-1] = first
        i++
    }
    console.log(arr)
}
reverseArr()

// Implement rotateArr(arr, shiftBy) that accepts array and offset.
// Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost.
// Operate in-place: given ([1,2,3],1), change the array to [3,1,2].
// Don't use built-in functions.
// Second: allow negative shiftBy (shift L not R).
// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions
// Fourth: minimize the touches of each element
function rotateArr(arr = [3,6,9,12,15,18,21,24], shiftBy=3) {
    len = arr.length
    i = 0
    first_idx = 0
    first_val = arr[first_idx]
    i = 1
    while (i < len + 1 && len >= shiftBy) {
        next_idx = first_idx + shiftBy
        if (next_idx >= len) {
            next_idx = next_idx - len
        }
        next_val = arr[next_idx]
        arr[next_idx] = first_val
        
        first_val = next_val
        first_idx = next_idx
        i++
    }
    console.log(arr)
}
rotateArr([1,2,3],1)

// Alan is good at breaking secret codes. One method is to eliminate values
// that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order.
// No built-in array functions.
function filterRange(arr = [2,4,6,8,10,1,3,5,7,9,3,6,9,12,5,10,15,20],num_min=4, num_max=8) {
    console.log(arr)
    len = arr.length
    i = 0
    while (i < len) {
        if (arr[i] < num_min || arr[i] > num_max) {
            arr[i]= ""
        }
        i++
    }
    console.log(arr)
}
filterRange()

// Replicate Javascript's concat(). Create a standalone function that accepts two arrays.
// Return a new array containing the first array's elements, followed by the second array's elements.
// Do not alter the original arrays. Ex.: arrConcat(['a','b'], [1,2]) should return new array ['a','b',1,2].
function arrConcat(arr1=['a','b'], arr2=[1,2]) {
    arr1_len = arr1.length
    arr2_len = arr2.length

    arr = []
    i = 0
    j = 0
    while (i < arr1_len) {
        arr[j] = arr1[i]
        i++
        j++
    }

    i = 0
    while (i < arr2_len) {
        arr[j] = arr2[i]
        i++
        j++
    }
    console.log(arr)
}
arrConcat(['abc','def','a','b','c'],[45,56,67,1,3,4])