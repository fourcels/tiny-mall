from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from tiny_mall.database import Base
import uuid


class Category(Base):
    __tablename__ = "categories"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4,  primary_key=True)
    name = Column(String, unique=True)
    sort = Column(Integer, index=True, default=0)
    created_at = Column(DateTime, default=datetime.now, index=True)
