class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, Scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.Scores = Scores

    def printPerson(self):
        Person.printPerson(self)

    def calculate(self):
        calScores = 0
        i = 0
        while i < len(self.Scores):
            calScores += self.Scores[i]
            i += 1
        calScores = calScores/len(self.Scores)

        letter_grade = ""

        if calScores <= 39:
            letter_grade = "T"
        elif calScores <= 54:
            letter_grade = "D"
        elif calScores <= 69:
            letter_grade = "P"
        elif calScores <= 79:
            letter_grade = "A"
        elif calScores <= 89:
            letter_grade = "E"
        else:
            letter_grade = "O"
        #print(letter_grade)
        return(letter_grade)

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
