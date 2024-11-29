import uvicorn
from fastapi import FastAPI
from src.routing.location_router import location_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(location_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://roamtheworld.ru", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type", "X-Requested-With"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)