
def powerset(array):
    subsets = [[]]
    print("\n")
    for ele in array:
        for i in range(len(subsets)):
            print(f"Element {ele}, index {i}")
            print(f"State of subsets {subsets}")
            currentSubset = subsets[i]
            print(f"currentSubset is {currentSubset}")
            print(f"currentSubset with element added {currentSubset + [ele]}")
            subsets.append(currentSubset + [ele])
            print(f"State of subsets through index {i}: {subsets}\n")
    return subsets

array = [1,2]
print(f"Final array: {powerset(array)}\n")