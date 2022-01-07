from tiny_mall.database import SessionLocal
from tiny_mall.config import settings
from tiny_mall import cruds, schemas

import click


@click.group()
def cli():
    pass


@cli.command()
def init_admin():
    with SessionLocal() as db:
        db_user = cruds.user.get_user_by_username(db, settings.admin_username)
        if not db_user:
            user = schemas.UserCreate(
                username=settings.admin_username,
                password=settings.admin_password,
                role=schemas.UserRoleEnum.superadmin,
            )
            cruds.user.create_user(db, user)


if __name__ == '__main__':
    cli()
