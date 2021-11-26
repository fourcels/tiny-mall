from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.routing import APIRouter
from tiny_mall import deps, routers

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(routers.login.router, tags=['登录'])

admin_router = APIRouter(
    prefix='/admin', dependencies=[Depends(deps.get_current_active_admin)])
admin_router.include_router(
    routers.admin.category.router, tags=['admin - 商品分组'])
admin_router.include_router(
    routers.admin.product.router, tags=['admin - 商品'])
app.include_router(admin_router)

client_router = APIRouter(
    prefix='/client', dependencies=[Depends(deps.get_current_active_user)])
client_router.include_router(routers.client.user.router, tags=['client - 用户'])
client_router.include_router(
    routers.client.category.router, tags=['client - 商品分组'])
client_router.include_router(
    routers.client.address.router, tags=['client - 用户地址'])
client_router.include_router(
    routers.client.order.router, tags=['client - 订单'])
app.include_router(client_router)
