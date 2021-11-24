from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.routing import APIRouter
from tiny_mall import deps, routers
from tiny_mall.init import init_db

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(routers.login.router, tags=['登录'])

admin_router = APIRouter(
    prefix='/admin', dependencies=[Depends(deps.get_current_active_admin)])
admin_router.include_router(
    routers.admin.category.router, tags=['admin - 商品分组'])
app.include_router(admin_router)

client_router = APIRouter(
    prefix='/client', dependencies=[Depends(deps.get_current_active_user)])
client_router.include_router(routers.client.user.router, tags=['client - 用户'])
client_router.include_router(
    routers.client.category.router, tags=['client - 商品分组'])
app.include_router(client_router)
