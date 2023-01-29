from flask import jsonify, Blueprint

from dao.dao import PostsDAO
import logging


api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostsDAO('./data/posts.json', './data/comments.json')

logging.basicConfig(filename='basic.log', level=logging.INFO)
logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")

@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    return jsonify(posts.load_posts_json())

@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post_by_pk(post_id):
    return jsonify(posts.get_post_by_pk_json(post_id))