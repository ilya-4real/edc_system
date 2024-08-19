from litestar import Router, post


@post("register")
async def register_user() -> str: ...


auth_router = Router(path="auth", route_handlers=[register_user])
