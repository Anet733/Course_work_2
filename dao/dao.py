import json
from dao.post import Post


class PostsDAO:

    def __init__(self, posts_path, comments_path):
        """
        Инициализируем пути к файлам с постами и комментами
        """
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_posts(self):
        """
        Распаковка и преобразование в список объектов
        """
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)
            new_posts = []
            for post in posts_data:
                new_posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count'],
                    post['pk']))
            return new_posts

    def get_all_posts(self):
        """
        Выводим спиисок всех постов
        """
        return self.load_posts()

    def get_posts_by_pk(self, post_id):
        """
        Получаем пост по номеру
        """
        posts = self.load_posts()
        for post in posts:
            if post_id == post.pk:
                return post
        return

    def load_comments(self):
        """
        Распаковка файла с комментами
        """
        with open(self.comments_path, 'r', encoding='utf-8') as file:
            comments = json.load(file)
        return comments

    def get_comments_by_post_id(self,post_id):
        """
        Получаем пост по номеру
        """
        comments = self.load_comments()
        comments_for_post = []
        for comment in comments:
            if comment['post_id'] == post_id:
                comments_for_post.append(comment)
        return comments_for_post

    def search_posts(self, substr):
        """
        Поиск
        """
        posts = self.load_posts()
        found_posts = []
        for post in posts:
            if substr.lower() in post.content.lower():
                found_posts.append(post)
        return found_posts

    def get_posts_by_user_name(self, user_name):
        """
        Посты по пользователю
        """
        posts = self.load_posts()
        found_posts = []
        for post in posts:
            if user_name.lower() == post.poster_name.lower():
                found_posts.append(post)

        return found_posts

    def load_posts_json(self):
        """
        Преобразование в json для api
        """
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return  data

    def get_post_by_pk_json(self, post_id):
        """
        Получение файла json для api
        """
        posts = self.load_posts_json()
        for post in posts:
            if  post['pk'] == post_id:
                return post









