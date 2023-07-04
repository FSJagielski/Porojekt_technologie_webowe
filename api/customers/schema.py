from enum import Enum

from typing import Optional
from pydantic import BaseModel

class CustomerCreateSchema(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski",
                "email": "jan.kowalski@example.com",
                "phone_number": "000-000-000",
            }
        }

class CustomerUpdateSchema(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski"
            }
        }


class Customer(CustomerCreateSchema):
    id: int





# class StudentCreateSchema(BaseModel):
#     first_name: str
#     last_name: str

#     class Config:
#         schema_extra = {
#             "example": {
#                 "first_name": "Zbyszek",
#                 "last_name": "Kieliszek",
#             }
#         }

# class StudentUpdateSchema(BaseModel):
#     first_name: Optional[str]
#     last_name: Optional[str]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "first_name": "Zbysiu",
#             }
#         }


# class Student(StudentCreateSchema):
#     id: int
