from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)
articles = [
    {
        'id': 1,
        'title': 'the way to python',
        'content': 'tuple, list, dict'
    },
    {
        'id': 2,
        'title': 'the way to REST',
        'content': 'GET, POST, PUT'
    }
]
@app.route('/blog/api/articles', methods=['GET'])
def get_articles():
    """ 获取所有文章列表 """
    return jsonify({'articles': articles})

@app.route('/blog/api/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    """ 获取某篇文章 """
    # l = [ articles[x]["id"]  for x in range(len(articles))]

    article = list(filter(lambda a:a['id'] == article_id , articles ))
    if len(article) == 0:
        abort(404)
    return jsonify({'article': article[0]})

@app.route('/blog/api/articles', methods=['POST'])
def create_article():
    if not request.json or not 'title' in request.json:
        abort(400)
    article = {
        'id': articles[-1]['id'] + 1,
        'title': request.json['title'],
        'content': request.json.get('content', '')
    }
    articles.append(article)
    return jsonify({'article': article}), 201


@app.route('/blog/api/articles/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    article = list(filter(lambda a:a['id'] == article_id , articles ))
    if len(article) == 0:
        abort(404)
    if not request.json:
        abort(400)
    
    article[0]['title'] = request.json.get('title', article[0]['title'])
    articles[0]['content'] = request.json.get('content', articles[1]['content'])
    
    return jsonify({'article': article[0]})


# @app.route('/blog/api/articles/<int:article_id>', methods=['PUT'])
# def update_article(article_id):
#     l = [ articles[x]["id"]  for x in range(len(articles))]
#     if article_id not in l :
#         abort(404) 
#     if not request.json:
#         abort(400)
#     articles[article_id-1]['title'] = request.json.get('title', articles[article_id - 1]['title'])
#     articles[article_id-1]['content'] = request.json.get('content', articles[article_id - 1]['content'])
#     return jsonify({'article': articles[article_id - 1]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)