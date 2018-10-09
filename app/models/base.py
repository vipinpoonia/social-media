import uuid
from datetime import datetime
from sqlalchemy_utils import UUIDType

from app import db


class BaseModelMixin(db.Model):
    __abstract__ = True

    id = db.Column(
        UUIDType(binary=False),
        primary_key=True,
        nullable=False,
        default=uuid.uuid1
    )
    created_on = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )
    updated_on = db.Column(
        db.DateTime, nullable=False,
        onupdate=datetime.now,
        default=datetime.now
    )
