from flask import render_template, Blueprint, request
from dao.dao import PostsDAO


main_blueprint = Blueprint('main-blueprint', __name__, template_folder="./templates")
posts = PostsDAO('./data/posts.json', './data/comments.json')


@main_blueprint.route('/')
def page_index():
    all_posts = posts.get_all_posts()
    return render_template('index.html', posts=all_posts)

@main_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    found_post = posts.get_posts_by_pk(post_id)
    comments = posts.get_comments_by_post_id(post_id)
    return render_template('post.html', post=found_post, comments=comments)

@main_blueprint.route('/search')
def search_page():
    query = request.args.get('s')
    found_posts = posts.search_posts(query)
    return render_template('search.html', posts=found_posts)

@main_blueprint.route('/users/<user_name>')
def user_page(user_name):
    user_posts = posts.get_posts_by_user_name(user_name)
    return render_template('user-feed.html', posts=user_posts, username=user_name)







