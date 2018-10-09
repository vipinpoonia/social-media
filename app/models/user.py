from enum import Enum

from sqlalchemy.orm import load_only
from sqlalchemy_utils import ChoiceType
from sqlalchemy import String

from .base import BaseModelMixin
from .follow import Follow
from app import db


class User(BaseModelMixin):
    __table_name__ = 'user'

    class Gender(Enum):
        MALE = 'M'
        FEMALE = 'F'
        OTHER = 'O'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    # user profile pic url
    avatar = db.Column(db.String(400))
    # cover image url
    cover = db.Column(db.String(400))
    gender = db.Column(
        ChoiceType(Gender, impl=String()),
        index=True
    )

    #   not using status for now assuming all as active.
    active = db.Column(db.Boolean(), default=False, index=True)
    #   created relationship with posts
    posts = db.relationship(
        'Post',
        backref='author',
        lazy='dynamic'
    )
    '''
        followers: people who follow User
        following: people whom user follow
    '''
    following = db.relationship(
        'User',
        secondary='follow',
        primaryjoin='User.id==follow.c.follower_id',
        secondaryjoin='User.id==follow.c.user_id',
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    '''
    can be used for employees.
        # is_staff = db.Column(db.Boolean(), default=False, index=True)
    
            not implemented can be used if phone number is stored 
        # _phone_number = db.Column(db.Unicode(20))
        # _country_code = db.Column(db.Unicode(8))
    
    not implementing login
        
        # password = db.Column(db.String(255), nullable=False)
    
    can be used for login implementation
        # @staticmethod
        # @login_manager.user_loader
        # def load_user(user_id):
        #     print(user_id)
        #     return User.query.get(user_id)
        
    '''

    def __str__(self):
        return self.username

    def __repr__(self):
        return "User(%s, %s)" % (
            str(self.first_name),
            str(self.last_name)
        )

    @property
    def following_count(self):
        return self.following.count()

    @property
    def post_count(self):
        return self.posts.count()

    @property
    def name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    @classmethod
    def create(cls, **kwargs):
        user = cls(
            first_name=kwargs.pop('first_name'),
            last_name=kwargs.pop('last_name'),
            username=kwargs.pop('username'),
            gender=kwargs.pop('gender'),
            email=kwargs.pop('email', None),
            avatar=kwargs.pop('avatar', None),
            cover=kwargs.pop('cover', None)
        )
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get_all(cls, exclude=None):
        query = cls.query
        if exclude and type(exclude) is not list:
            exclude = [exclude]
            query = query.filter(
                ~ User.id.in_(exclude)
            )
        return query.order_by(
            User.first_name,
            User.last_name
        ).all()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)

    def is_following(self, user_id):
        return bool(
            self.following.filter(
                Follow.user_id == user_id
            ).count()
        )

    @property
    def following_users_ids(self):
        return [str(user.id) for user in self.following.options(load_only('id'))]
    '''
        can't follow if already following the user or 
        following more than one user
    '''
    def can_follow(self, user_id):
        following_users = self.following.options(load_only(User.id)).all()
        return (
            len(following_users) < 2 and
            str(user_id) not in [
                str(user.id) for user in following_users
            ]
        )

    def follow(self, user):
        if not self.can_follow(user):
            return False, 'You can follow maximum of 2 users'
        self.following.append(user)
        db.session.commit()
        return True, ''

    def serialize(self, extra=False):
        serialized_obj = {
            'id': str(self.id),
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'gender': self.gender.value,
            'avatar': self.avatar,
            'is_active': self.active,
            'cover': self.cover
        }
        if extra:
            serialized_obj['following_count'] = self.following_count
        if extra:
            serialized_obj['post_count'] = self.post_count
        return serialized_obj
