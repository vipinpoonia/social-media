from flask import request
from .base import BaseAPIMethodView
from .error import HTTPForbidden
from app.models import User, Post


class UserAPIView(BaseAPIMethodView):
    error = ''

    def test_get(self, user_id):
        self.user = User.get_by_id(user_id)
        if not self.user:
            self.error = 'User does not exists'
            return False
        return True

    def get(self, *args, **kwargs):
        return {
            'status': 'success',
            'data': self.user.serialize(extra=True)
        }


'''
    not creating paginated api 
    also using the same api for getting following status for current user

    there should be 2 different Apis
        1. to get paginated users.
        2. to get followers of current logged in user
'''


class BulkUserAPIView(BaseAPIMethodView):
    error = ''

    def test_get(self):
        self.user_id = request.args.get('user_id')
        self.user = User.get_by_id(self.user_id) if self.user_id else None
        if self.user_id and not self.user:
            self.error = 'User does not exists'
            return False
        return True

    def get(self, *args, **kwargs):
        if self.user:
            users = User.get_all(exclude=self.user_id)

            '''
                If current user_id is present add the 
                following status for current user in serialized object
            '''
            following_users_ids = self.user.following_users_ids
            serialized_users = []
            for user in users:
                serialized_user = user.serialize()
                serialized_user['is_following'] = (
                    str(user.id) in following_users_ids
                )
                serialized_users.append(serialized_user)
            return {
                'status': 'success',
                'data': serialized_users
            }
        return {
            'status': 'success',
            'data': [user.serialize() for user in User.get_all()]
        }


# creating without pagination
class PostAPIView(BaseAPIMethodView):
    error = ''
    required_keys_get = [
        'user_id'
    ]
    required_keys_post = [
        'user_id', 'text'
    ]

    def check_user(self, user_id):
        self.user = User.get_by_id(user_id)
        if not self.user:
            self.error = 'User does not exists'
            return False
        return True

    def test_get(self):
        return self.check_user(request.args.get('user_id'))

    def get(self, *args, **kwargs):
        return {
            'status': 'success',
            'data': Post.get_serialized_posts_for_user(self.user)
        }

    def test_post(self):
        return self.check_user(request.json.get('user_id'))

    def post(self, *args, **kwargs):
        post = Post.create(**request.json)
        return {
            'data': post.serialize(),
            'status': 'success'
        }


class FollowAPIView(BaseAPIMethodView):
    required_keys_post = [
        'follow_user_id'
    ]

    def test_post(self, user_id):
        follow_user_id = request.json.get('follow_user_id')

        self.user = User.get_by_id(user_id)
        if not self.user:
            self.error = 'User does not exists'
            return False

        self.follow_user = User.get_by_id(follow_user_id)
        if not self.follow_user:
            self.error = 'Followed user does not exists'
            return False
        return True

    def post(self, *args, **kwargs):
        status, message = self.user.follow(self.follow_user)
        if not status:
            raise HTTPForbidden(message=message)
        return {
            'status': 'success',
        }
