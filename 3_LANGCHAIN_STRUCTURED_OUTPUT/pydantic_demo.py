from pydantic import BaseModel , EmailStr ,  Field
from typing import Optional
# Pydantic is a data validation and settings management library for Python, which uses Python type annotations.
# It allows you to define data models with type annotations, and it automatically validates the data against those types.

#type coerce = change the type of a value to another type, if possible
class Student(BaseModel):
    name:str = 'sujal' # default value for name is 'sujal'
    age: Optional[int] = None # age is optional, can be None
    email : EmailStr # email must be a valid email address    
    cgpa : float = Field(gt=0, lt=10,default=9,description='a decimal value representing cgpa') # cgpa must be greater than 0 and less than 10

new_student = {'age': 20, 'email': 'abc@gmail.com','cgpa':8.24}  # 'name' is not provided, so it will use the default value 'sujal'
# throws error if email is not valid
# If 'name' is not provided, it will use the default value 'sujal'
student  = Student(**new_student)
print(student)
print(type(student)) 

student_dict = dict(student) # convert the Pydantic model to a dictionary
print(student_dict['age'])

student_json = student.model_dump_json()# convert the Pydantic model to a JSON string
