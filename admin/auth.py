from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminConfig, AdminUser, AuthProvider
from starlette_admin.exceptions import LoginFailed

from database import User


class UsernameAndPasswordProvider(AuthProvider):
    async def login(
            self,
            username: str,
            password: str,
            remember_me: bool,
            request: Request,
            response: Response,
    ) -> Response:
        email = username
        user = await User.get_by_email(email)

        if not user:
            raise LoginFailed("Invalid email or password")

        if user.role != User.Role.ADMIN:
            raise LoginFailed("You are not allowed to access admin panel")

        if not user.check_password(password):
            print(password)
            raise LoginFailed("Invalid email or password")

        request.session.update({"email": email})
        request.state.user = user
        return response

    async def is_authenticated(self, request: Request) -> bool:
        email = request.session.get("email")
        if not email:
            return False

        user = await User.get_by_email(email)
        if not user:
            return False

        request.state.user = user
        return True

    def get_admin_config(self, request: Request) -> AdminConfig:
        user: User = request.state.user
        return AdminConfig(app_title=f"Hello, {user.username}!")

    def get_admin_user(self, request: Request) -> AdminUser:
        user: User = request.state.user
        return AdminUser(username=user.email)

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response
