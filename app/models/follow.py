from sqlalchemy_utils import UUIDType
from .base import BaseModelMixin
from app import db


class Follow(BaseModelMixin):
    __table_name__ = 'follow'
    '''
        user id is the id of person being followed by other 
    '''
    user_id = db.Column(
        UUIDType(),
        db.ForeignKey('user.id'),
        nullable=False
    )
    follower_id = db.Column(
        UUIDType(binary=False),
        db.ForeignKey('user.id'),
        nullable=False
    )


    '''
        not adding followed_on because posted_on will be 
        same as created on 
    '''

    @classmethod
    def create(cls, **kwargs):
        follow = cls(
            user_id=kwargs.pop('user_id'),
            follower_id=kwargs.pop('follower_id'),
        )
        db.session.add(follow)
        db.session.commit()
        return follow
