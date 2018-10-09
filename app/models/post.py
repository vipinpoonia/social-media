from enum import Enum
from sqlalchemy import String, desc
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils import ChoiceType


from .base import BaseModelMixin
from app import db


class Post(BaseModelMixin):
    __table_name__ = 'post'

    class ContentType(Enum):
        IMAGE = 'IMG'
        VIDEO = 'VID'
        URL = 'URL'

    user_id = db.Column(
        UUIDType(),
        db.ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False
    )

    text = db.Column(
        db.String(10000),
        nullable=False
    )
    # image and video urls
    _content = db.Column('content', db.String(400))
    _content_type = db.Column(
        'content_type',
        ChoiceType(ContentType, impl=String()),
        index=True
    )
    '''
        not adding posted_on because posted_on will be 
        same as created on 
    '''

    @property
    def content(self):
        return self._content

    @property
    def content_type(self):
        return self._content_type.value if self._content_type else None

    @classmethod
    def create(cls, **kwargs):
        post = cls(
            user_id=kwargs.pop('user_id'),
            text=kwargs.pop('text'),
            _content=kwargs.pop('content', None),
            _content_type=kwargs.pop('content_type', None)
        )
        db.session.add(post)
        db.session.commit()
        return post

    @classmethod
    def filter_by_user_ids(cls, user_ids):
        return cls.query.filter(
            Post.user_id.in_(user_ids)
        ).order_by(desc(Post.created_on)).all()

    def serialize(self):
        return {
            'id': str(self.id),
            'user_id': str(self.user_id),
            'text': self.text,
            'content': self.content,
            'content_type': self.content_type,
            'created_on': self.created_on.strftime("%H:%M, %d %b %Y")
        }

    @classmethod
    def get_serialized_posts_for_user(cls, user):
        user_id_to_avatar_map = {
            user.id: user.avatar
        }
        user_id_to_author_map = {
            user.id: user.name
        }
        for following in user.following.all():
            user_id_to_avatar_map[following.id] = following.avatar
            user_id_to_author_map[following.id] = following.name
        posts = cls.filter_by_user_ids(list(user_id_to_avatar_map.keys()))
        serialized_posts = []
        for post in posts:
            serialized_post = post.serialize()
            serialized_post['avatar'] = user_id_to_avatar_map[post.user_id]
            serialized_post['author'] = user_id_to_author_map[post.user_id]
            serialized_posts.append(serialized_post)
        return serialized_posts
