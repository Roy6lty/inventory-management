import string
from sqlalchemy import (
    DATE,
    Integer,
    String,
    Boolean,
    ForeignKey,
    TIMESTAMP,
    Index,
    TEXT,
    FLOAT,
    text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from sqlalchemy.orm import declarative_base
from sqlalchemy.types import UUID
from sqlalchemy.sql import func
from datetime import datetime, date, timedelta
import uuid

Base = declarative_base()
from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSON, JSONB


class UserData_tbl(Base):
    __tablename__ = "User_data"
    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
