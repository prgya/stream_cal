from fastapi import FastAPI 
from calculator import calculate
from pydantic import BaseModel

class User_Input(BaseModel):
    operation: str
    a: int
    b: int

app = FastAPI()

@app.post('/calculate')
def operate(input:User_Input):
    return calculate(input.operation, input.a, input.b)