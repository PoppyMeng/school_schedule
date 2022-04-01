from school_schedule.student import Student, has_more_class

#first instance
quinn = Student(
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
                "Grace Hopper"
            )

quinn.add_class("Painting")
quinn.get_num_classes()
quinn.summary()
print(vars(quinn))
# second instance
claire = Student(
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

claire.get_num_classes()
claire.summary()
claire.has_a_specific_class("Art")
# Extra:
# - create a function that will return the student with more classes
has_more_class(claire, quinn)
# - create a test for that function