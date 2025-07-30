from fastapi import FastAPI

app = FastAPI()

def add_numbers(a: int, b: int) -> int:
    return a + b

@app.get("/add")
async def add(a: int, b: int):
    result = add_numbers(a, b)
    return {"result": result}