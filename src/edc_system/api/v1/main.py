from litestar import Litestar, Router
from litestar.middleware import DefineMiddleware
from litestar.openapi import OpenAPIConfig

from src.edc_system.api.v1.auth.routes import auth_router
from src.edc_system.api.v1.middlewares.auth_middleware import CustomJWTAuth

auth_mw = DefineMiddleware(CustomJWTAuth, exclude="schema")

openapi_config = OpenAPIConfig(
    title="Electronic Digital Signature system",
    version="0.1.0",
    description="System that helps to sign and verify any kind of files",
)

base_router = Router("v1", route_handlers=[auth_router])

application = Litestar(
    route_handlers=[base_router],
    middleware=[auth_mw],
    openapi_config=openapi_config,
)
