'''
NOTAS
Paso 1: Identifico el tamaño de la entrada n
El tamaño de la entrada es el numero de 
estudiantes
2: Es ver cuanto crece el numero de operaciones
en mi algoritmo conforme crece el tamaño de 
la entrada 
'''

# Crando una lista de estudiantes 
student_list_01 = ['jordan', 'pipen', 'curry', 'Shac']
student_list_02 = ['Kyrie', 'Irving', 'Kobe', 'Bryant']

# Verificando presencia del estudiante
def check_stundent(input_student, student_list):
    for student in student_list:
        if input_student == student:
            print("Estudiante encontrado")
            return student
        # Si no encuentro al estudiante
        print("Estudiante no encontrado")
        return None
# Probando algoritmo
check_stundent("Kyrie", student_list_02)

