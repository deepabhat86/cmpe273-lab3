import random 
from random import randint

students=[]
classes=[]
students.append({"id": "1", "name":"Bob"})
classes.append({"id": "1", "name":"CMPE273", "students":[]})
RAND_MAX=10000
RAND_MIN=1

def generate_id():
    return random.randint(RAND_MIN,RAND_MAX)

def get_student(_, _info, id):
    for student in students:
        if student.get('id')==id:
            return student

def create_student(_, _info,input):
    id=str(generate_id())
    students.append({"id":id, "name":input["name"]})
    return {"id":id, "name":input["name"]}

def get_class(_, _info, id):
    for cl in classes:
        if cl.get("id")==id:
            return cl

def create_class(_,_info,input):
    id=str(generate_id())
    classes.append({"id":id, "name":input["name"], "students":[]})
    return {"id":id, "name":input["name"], "students":[]}

def update_class(_,_info,input):
    student_to_add={}
    #find the student to add based on the id provided in the mutation
    for student in students:
        if student.get('id')==input["studentid"]:
            student_to_add=student
            break
    list_of_students=[]
    for cl in classes:
        if cl.get("id")==input["id"]:
            list_of_students=cl.get("students")
            #check if student is already in class, if yes do not add
            for student in list_of_students:
                if student.get('id')==input["studentid"]:
                    return cl
            #add to list of students
            list_of_students.append(student_to_add)
            return cl
            
    
