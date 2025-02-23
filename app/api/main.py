from fastapi import FastAPI

app = FastAPI(title="Code Fusion")

@app.get("/")
async def root():
    return {"message": "Welcome to Code Fusion"}
