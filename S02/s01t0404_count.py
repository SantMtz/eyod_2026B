student_list_01 = ['jordan', 'pipen', 'curry', 'Shac'] #?

def random_function(students):
    first = students[0] #?
    total = 0 #?
    new_list = [] #?

    for student in students:
        total += 1 #?
        new_list.append(student) #?
        print(new_list) #?
        return total #?

print(random_function(student_list_01))