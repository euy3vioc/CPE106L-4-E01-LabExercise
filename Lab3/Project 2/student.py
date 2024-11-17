import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """Initialize the student with random scores."""
        self.name = name
        self.scores = [random.randint(0, 100) for _ in range(number)]

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def compareStudents(self, other):
        return self.scores == other.scores
    
    def lessThanStudent(self, other):
        return self.scores < other.scores
    
    def greatOrEqualStudent(self, other):
        return self.scores >= other.scores

    def __str__(self):
        """Returns the string representation of the student."""
        return self.name + "\nScores: " + " ".join(map(str, self.scores))

    def __lt__(self, other):
        """Defines the less-than operator for sorting."""
        return self.getAverage() < other.getAverage()

def main():
    students = [
        Student("Charles", 5),
        Student("Carlos", 5),
        Student("Josh", 5),
        Student("Alice", 5),
        Student("Bob", 5),
    ]

    print("Before shuffling and sorting:")
    for student in students:
        print(student)
        print()

    random.shuffle(students)

    print("After shuffling:")
    for student in students:
        print(student)
        print()

    students.sort()

    print("After sorting:")
    for student in students:
        print(student)
        print()

if "_name_" == "_main_":
    main()