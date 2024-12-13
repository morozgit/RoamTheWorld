from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from src.config.db.session import async_session_maker
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from src.models.models import User


class BasicAuth(AuthenticationBackend):
    def __init__(self, secret_key: str, default_username: str, default_password: str):
        super().__init__(secret_key)
        self.default_username = default_username
        self.default_password = default_password

    async def login(self, request: Request) -> RedirectResponse:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        async with async_session_maker() as session:
            query = select(User).where(User.name == username)
            result = await session.execute(query)
            user = result.scalar_one_or_none()

            if user:
                if user.password == password:
                    request.session.update({"user_id": user.id})
                    return RedirectResponse(request.url_for("admin:index"), status_code=302)
                else:
                    return RedirectResponse(request.url_for("admin:login"), status_code=302)

            if username == self.default_username and password == self.default_password:
                new_user = User(name=username, password=password)
                try:
                    session.add(new_user)
                    await session.commit()
                    request.session.update({"user_id": new_user.id})
                except IntegrityError:
                    await session.rollback()
                    return RedirectResponse(request.url_for("admin:login"), status_code=302)

                return RedirectResponse(request.url_for("admin:index"), status_code=302)

        return RedirectResponse(request.url_for("admin:login"), status_code=302)

    async def logout(self, request: Request) -> RedirectResponse:
        request.session.clear()
        return RedirectResponse(request.url_for("admin:login"), status_code=302)

    async def authenticate(self, request: Request) -> bool:
        return "user_id" in request.session
