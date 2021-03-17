import os
import requests
from requests.auth import HTTPBasicAuth
from sqlalchemy import create_engine, Table, MetaData
from operator import itemgetter


class Bot:
    def __init__(self):
        # database
        dr_url = os.path.dirname(os.path.realpath(__file__))
        d_url = f'sqlite:////{dr_url}/db.sqlite3'
        self.engine = create_engine(d_url)
        self.conn = self.engine.connect()
        self.meta = MetaData()
        self.exec = self.conn.execute
        self.table = Table('user_posts_count', self.meta, autoload=True, autoload_with=self.engine)
        # requests
        self.payload = {'email': 'admin@gmail.com', 'password': 'rootroot'}
        self.url = 'http://0.0.0.0:8080/api/v1/'
        self.user_list = 'users/list/'
        self.posts_list = 'posts/list/'

    def number_of_users(self):
        url = f'{self.url}{self.user_list}'
        r = requests.get(url, auth=HTTPBasicAuth(self.payload['email'], self.payload['password']))
        return f"Number Of Users:{r.json()['count']}"

    def max_posts_per_user(self):
        # Set of each user to 0
        self.exec(self.table.update().values(posts=0))
        # defining url and making request, taking from request only "request" key
        url = f'{self.url}{self.posts_list}'
        r = requests.get(url, auth=HTTPBasicAuth(self.payload['email'], self.payload['password'])).json()
        results = r['results']
        # looping threw every result
        for result in results:
            # Executing only users if database
            users_query = self.table.select()
            owner = result['owner']
            users = [user_info[1] for user_info in self.exec(users_query).fetchall()]
            if owner not in users:
                # Add user into database with value 1 if user not in database
                print('Added new user into database')
                add_user = self.table.insert().values(user=owner, posts=self.table.c.posts + 1)
                self.exec(add_user)
                print('User Executed')
                continue
            else:
                # increase user's post to 1
                plus_query = self.table.update().where(self.table.c.user == owner).values(posts=self.table.c.posts + 1)
                self.exec(plus_query)
                continue
        ended_list = max(self.exec(self.table.select()).fetchall(), key=itemgetter(2))

        return f'User {ended_list[1]} has maximum value of posts: {ended_list[2]}'


