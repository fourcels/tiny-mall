# 商家管理后端接口
主要涉及技术栈 [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/),
[docker](https://www.docker.com/)

## 相关地址
* [管理后台演示](https://admin.fourcels.com/) 用户名: guest, 密码: guest

* [接口文档](https://api.fourcels.com/docs)

* [管理后台API](https://github.com/fourcels/tiny-mall)

* [管理后台UI](https://github.com/fourcels/tiny-mall-admin-ui)

## 开发

1. [poetry](https://python-poetry.org/) 安装依赖
    ```bash
    poetry install
    poetry shell
    ```

1. [alembic](https://alembic.sqlalchemy.org/en/latest/) 初始化数据库
    ```bash
    alembic upgrade head
    python db.py init-admin
    ```
1. 启动
    ```bash
    python start.py -r
    ```