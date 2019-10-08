class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.intDiffs = []
        i = 0
        while i < len(self.__elements):
            j = i + 1
            while j < len(self.__elements):
                self.intDiffs.append(abs(self.__elements[i]-self.__elements[j]))
                j += 1

            i += 1
        self.maximumDifference = max(self.intDiffs)

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
