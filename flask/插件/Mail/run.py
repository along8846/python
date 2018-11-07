from flask import Flask
from flask_mail import Mail, Message
from threading import Thread
import os

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.126.com',  # 邮件服务器地址
    MAIL_PORT = 25,               # 邮件服务器端口
    MAIL_USE_TLS = True,          # 启用 TLS
    MAIL_USERNAME =  'ywl444@126.com',
    MAIL_PASSWORD =  '88461296ywl',
    MAIL_DEBUG = True

)


mail = Mail(app)

@app.route('/attach')
def index():
    msg = Message('Hi', sender='18628076761@126.com', recipients=['18628076761@126.com'])
    msg.html = '<b>Hello Web</b>'
    # msg.body = 'The first email!'
    with app.open_resource("/Users/apple/Desktop/1528965444467.jpg") as fp:
        msg.attach("along.jpg", "image/jpeg", fp.read())
    mail.send(msg)
    return '<h1>OK!</h1>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)