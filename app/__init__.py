from urllib.parse import quote

import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)

app.secret_key = 'kfshafeoiuhfweiafhewuo12312@!78235217841'
app.config['SQLALCHEMY_DATABASE_URI'] = str.format('mysql+pymysql://root:%s@localhost/hoteldb?charset=utf8mb4'
                                                   % quote('123456'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 4

db = SQLAlchemy(app=app)

cloudinary.config(
    cloud_name='dviegqpn6',
    api_key='429111181591928',
    api_secret='nfy9uHSyu4PwkjFiDh_MnJeNT70'
)

# Các thông số cần thiết từ tài khoản VNPay Sandbox
vnpay_config = {
    'vnp_TmnCode': 'PMAKVMOW',
    'vnp_HashSecret': 'USYEHCIUSVVCFQYKBQBZSUASXUXRSTCS',
    'vnp_Url': 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html',
}
