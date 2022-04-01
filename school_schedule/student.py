from codecs import getincrementaldecoder


class Student:
    def __init__(self, name, grade_level, class_list):
        self.name = name
        self.grade_level = grade_level
        self.class_list = class_list
        self.school_name = "Ada developers Academy"
    def add_class(self, course):
        self.class_list.append(course)
    def get_num_classes(self):
        return  len(self.class_list)
    def summary(self):
        print(f"{self.name} is in {self.grade_level} grade and has {len(self.class_list)} courses. ")

    def has_a_specific_class(self, specific_class):
        return specific_class in self.class_list

def has_more_class(s1, s2):
    if len(s1.get_num_classes())>len(s2.get_num_classes()):
        return s1 
    return s2
    
