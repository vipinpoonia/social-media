from app.models import *


def create_users():
    dummy_data = [
        {
            'avatar': 'https://raw.githubusercontent.com/Ashwinvalento/cartoon-avatar/master/lib/images/female/45.png',
            'email': 'seeva5@gmail.com',
            'first_name': 'Priya',
            'last_name': 'Singh',
            'username': 'priya.singh',
            'gender': 'F',
            'cover': 'https://picsum.photos/600/300?image=33',
            'posts': [
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "
                            "deserunt mollit anim id est laborum."
                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna ",
                    'content_type': 'IMG',
                    'content': 'https://picsum.photos/600/400?image=212'
                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "
                            "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                            "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                            "Duis aute irure dolor in reprehenderit in voluptate velit "

                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "

                },
            ]

        },
        {
            'avatar': 'https://raw.githubusercontent.com/Ashwinvalento/cartoon-avatar/master/lib/images/male/5.png',
            'email': 'aman55@gmail.com',
            'first_name': 'Aman',
            'last_name': 'Kumar',
            'username': 'aman55',
            'gender': 'M',
            'cover': 'https://picsum.photos/600/300?image=31',
            'posts': [
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "
                            "deserunt mollit anim id est laborum."
                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna ",
                    'content_type': 'IMG',
                    'content': 'https://picsum.photos/600/400?image=212'
                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "
                            "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                            "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                            "Duis aute irure dolor in reprehenderit in voluptate velit "

                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "

                },
            ]

        },
        {
            'avatar': 'https://raw.githubusercontent.com/Ashwinvalento/cartoon-avatar/master/lib/images/male/45.png',
            'email': 'vipin@gmail.com',
            'first_name': 'Vipin',
            'last_name': 'Kumar',
            'username': 'vipin',
            'gender': 'M',
            'cover': 'https://picsum.photos/600/300?image=34',
            'posts': [
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "
                            "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                            "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                            "Duis aute irure dolor in reprehenderit in voluptate velit "
                            "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "

                },
                {
                    'text': "Duis aute irure dolor in reprehenderit in voluptate velit "
                            "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
                            "occaecat cupidatat non proident, sunt in culpa qui officia "
                            "deserunt mollit anim id est laborum."
                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    'content_type': 'IMG',
                    'content': 'https://picsum.photos/600/400?image=400'

                },
            ]
        },
        {
            'avatar': 'https://raw.githubusercontent.com/Ashwinvalento/cartoon-avatar/master/lib/images/male/1.png',
            'email': 'mohit@gmail.com',
            'first_name': 'Mohit',
            'last_name': 'Garg',
            'username': 'mohit',
            'gender': 'M',
            'cover': 'https://picsum.photos/600/300?image=35',
            'posts': [
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit,",
                    'content_type': 'IMG',
                    'content': 'https://picsum.photos/600/400?image=401'
                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "
                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "
                            "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                            "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                            "Duis aute irure dolor in reprehenderit in voluptate velit "

                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "

                },
            ]
        },
        {
            'avatar': 'https://raw.githubusercontent.com/Ashwinvalento/cartoon-avatar/master/lib/images/male/2.png',
            'email': 'sid@gmail.com',
            'first_name': 'Sidharth',
            'last_name': 'Jain',
            'username': 'sid',
            'gender': 'M',
            'cover': 'https://picsum.photos/600/300?image=37',
            'posts': [
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "
                            "deserunt mollit anim id est laborum."
                },
                {
                    'text': "Sed do eiusmod tempor incididunt ut labore et dolore magna.",
                            'content_type': 'IMG',
                            'content': 'http://www.gstatic.com/webp/gallery/5.jpg'
                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                            "Duis aute irure dolor in reprehenderit in voluptate velit "

                },
                {
                    'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                            "sed do eiusmod tempor incididunt ut labore et dolore magna "

                },
            ]
        }

    ]

    for data in dummy_data:
        posts = data.pop('posts')
        user = User.create(**data)
        for post in posts:
            post['user_id'] = str(user.id)
            Post.create(**post)
    return True
