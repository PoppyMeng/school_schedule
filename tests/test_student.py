from school_schedule.student import Student


def test_instance_attributes_are_correct():
    result = Student(
        "Quinn",
        "junior",
        [
            "Pre-Calc",
            "English III",
            "World History",
            "Gym",
            "Chemistry",
            "Music Composition"
        ]
    )

    assert result.name == "Quinn"
    assert result.grade_level == "junior"
    assert result.class_list == ["Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition"]


def test_correct_class_added():
    s = Student(
        "Claire",
        "freshmen",
        [
            "Algebra",
            "Writing",
            "Contemporary Issues",
            "Gym",
            "Earth Science",
            "Painting"
        ]
    )
    s.add_class("Art")

    assert len(s.class_list) == 7


def test_if_list_classes_empty_return_empty_list():
    result = Student(
        "Quinn",
        "junior",
        []
    )

    assert result.class_list == []