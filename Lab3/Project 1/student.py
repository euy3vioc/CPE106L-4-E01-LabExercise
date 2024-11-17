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


def main():
    student1 = Student("Charles", 1)
    student2 = Student("Carlos", 1)
    student3 = Student("Josh", 1)

    print("Student 1:", student1)
    print("\nStudent 2:", student2)
    print("\nStudent 3:", student3)

    print("\nEquality Test: \n")
    print("Are students 1 and 2 equal?", student1.compareStudents(student2))
    print("Is student 1 less than student 2?", student1.lessThanStudent(student2))
    print("Is student 1 greater than or equal to student 2?", student1.greatOrEqualStudent(student2))

if __name__ == "__main__":
    main()