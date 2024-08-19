from litestar.connection import ASGIConnection
from litestar.exceptions import NotAuthorizedException
from litestar.middleware import AbstractAuthenticationMiddleware, AuthenticationResult


class CustomJWTAuth(AbstractAuthenticationMiddleware):
    async def authenticate_request(
        self, connection: ASGIConnection
    ) -> AuthenticationResult:
        auth_header = connection.headers.get("Authorization")

        # if not auth_header:
        # raise NotAuthorizedException

        return AuthenticationResult("user", "key")
