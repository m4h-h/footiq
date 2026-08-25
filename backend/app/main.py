from fastapi import FastAPI

app = FastAPI(title="FootIQ API")


@app.get("/")
def root():
    return {"message": "Welcome to FootIQ API"}