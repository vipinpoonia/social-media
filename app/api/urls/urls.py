from app import app
from app.api.views import UserAPIView, BulkUserAPIView, PostAPIView, FollowAPIView


user_api_view = UserAPIView.as_view('user_api')
app.add_url_rule(
    '/demoapp/users/<uuid:user_id>/',
    view_func=user_api_view,
    methods=['GET']
)

bulk_user_api_view = BulkUserAPIView.as_view('bulk_user_api')
app.add_url_rule(
    '/demoapp/users/',
    view_func=bulk_user_api_view,
    methods=['GET']
)

bulk_post_view = PostAPIView.as_view('bulk_post_api')
app.add_url_rule(
    '/demoapp/posts/',
    view_func=bulk_post_view,
    methods=['GET', 'POST']
)

follow_api_view = FollowAPIView.as_view('follow_api')
app.add_url_rule(
    '/demoapp/users/<uuid:user_id>/follow/',
    view_func=follow_api_view,
    methods=['POST']
)