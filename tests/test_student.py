from school_schedule.student import Student

# Write your tests here!
def test_student_innitial_instance():
    # Arrange
    name = "Quinn"
    grade = "junior"
    classes = ["Pre-Calc", 
            "English III", 
            "World History", 
            "Gym", 
            "Chemistry", 
            "Music Composition"
                ]
    
    # Act
    student = Student(name,grade,classes)

    # Assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes


def test_add_two_class():
    # Arrange
    name = "Quinn"
    grade = "junior"
    classes = ["Pre-Calc", 
            "English III", 
            "World History", 
            "Gym", 
            "Chemistry", 
            "Music Composition"
                ]
    
    student = Student(name,grade,classes)

    # Act
    result = student.add_class(["Painting","Writing"])

    # Assert
    assert result == ["Pre-Calc", 
            "English III", 
            "World History", 
            "Gym", 
            "Chemistry", 
            "Music Composition",
            "Painting",
            "Writing"]
    

def test_length_of_classes_with_empty_classes():
    # Arrange
    name = "Quinn"
    grade = "junior"
    classes = []
    
    student = Student(name,grade,classes)

    # Act
    result = student.get_num_classes()

    # Assert
    assert result == 0



