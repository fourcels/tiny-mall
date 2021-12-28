from fastapi import FastAPI, Depends
from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from tiny_mall import deps, routers
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse
from starlette.middleware.errors import ServerErrorMiddleware


app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Total"]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(routers.user.router, tags=['用户'])
app.include_router(routers.file.router, tags=['上传'])

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
