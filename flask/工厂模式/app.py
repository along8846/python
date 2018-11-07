from flask import Flask, render_template
from book import book
from movie import movie
from configs import config


def create_app(config_name):
    app = Flask(__name__)

    # basic config
    app.config.from_object(config[config_name])

    # blueprints
    app.register_blueprint(book.book_bp)
    app.register_blueprint(movie.movie_bp)

    # error handler
    handle_errors(app)

    return app

def handle_errors(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

# app = Flask(__name__)
# app.secret_key = 'The quick brown fox jumps over the lazy dog'

# # 注册蓝图
# app.register_blueprint(book.book_bp)
# app.register_blueprint(movie.movie_bp)

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404


# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)