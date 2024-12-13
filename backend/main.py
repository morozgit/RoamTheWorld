import uvicorn
from fastapi import FastAPI
from src.routing.location_router import location_router
from src.routing.track_router import track_router
from fastapi.middleware.cors import CORSMiddleware
import rollbar
from rollbar.contrib.fastapi import add_to as rollbar_add_to
from src.config.environment import settings
from sqladmin import Admin
from src.config.db.session import engine
from auth.admin import UserAdmin, auth_backend, LocationAdmin, TrackAdmin

app = FastAPI(
    title="RoamTheWorld API documentation",
)

rollbar.init(access_token=settings.ROLLBAR_ACCESS_TOKEN, environment="production")
rollbar_add_to(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://roamtheworld.ru", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type", "X-Requested-With"],
)

app.include_router(location_router)
app.include_router(track_router)
admin = Admin(app=app, engine=engine, authentication_backend=auth_backend)
admin.add_view(UserAdmin)
admin.add_view(LocationAdmin)
admin.add_view(TrackAdmin)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
