from typing import List
from fastapi import APIRouter, HTTPException
from .model import Student, StudentUpdate
from .data import students

student_router = APIRouter()

@student_router.get("/")
def get_students():
    return students

@student_router.get("/{student_id}")
def get_student(student_id: int):
    student = [student for student in students if student['id'] == student_id]
    if not student:
        return HTTPException(status_code=404, detail="Student not found")
    return student

@student_router.post("/")
def create_student(new_student: Student):
    if any([ (student['id'] == new_student.id) for student in students ]):
        return HTTPException(status_code=400, detail="Student already registered")
    students.append(new_student.model_dump())
    return new_student

@student_router.put("/{student_id}")
def update_student(student_id: int, student_update: StudentUpdate):
    found = None
    for student in students:
        if student['id'] == student_id:
            found = student
            break
    if not found:
        return HTTPException(status_code=404, detail="Student not found")
    found['nombre'] = student_update.nombre
    found['matricula'] = student_update.matricula
    return found

@student_router.delete("/{student_id}")
def delete_student(student_id: int):
    new_students = []
    found = False
    for i, student in enumerate(students):
        if student['id'] == student_id:
            students.pop(i)
            found = True
            break 
    if not found:
        return HTTPException(status_code=404, detail="Student not found")
    return students