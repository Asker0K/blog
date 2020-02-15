from flask_admin.contrib.sqla import ModelView
from app.models import User, Post
from app import admin, db


class UserView(ModelView):
    # can_delete = False  # disable model detection
    column_exclude_list = ['token', 'token_expiration', 'last_message_read_time',
                           'followed', 'messages_sent', 'messages_received',
                           'notifications', 'tasks', 'password_hash']

    form_excluded_columns = ['token', 'token_expiration', 'last_message_read_time',
                             'followed', 'messages_sent', 'messages_received',
                             'notifications', 'tasks', 'last_seen',
                             'last_message_read time', 'password_hash', 'followers', 'posts']


class PostView(ModelView):
    page_size = 10  # the number of entries to display on the list view
    form_excluded_columns = ['language']


admin.add_view(UserView(User, db.session))
admin.add_view(PostView(Post, db.session))
