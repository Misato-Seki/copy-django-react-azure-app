# 「os」を使うと、プログラムがファイルを操作したり、フォルダの場所を知ることができる
import os
from .settings import *
from .settings import BASE_DIR

# ウェブサイトがどこで動くかを決める
# os.environ['WEBSITE_HOSTNAME']は、コンピュータやサーバーの中に隠されている環境変数からその名前を取り出す
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

# CSRF（クロスサイトリクエストフォージェリ）という攻撃から守るための設定
# CSRF_TRUSTED_ORIGINSは、「信頼できるウェブサイトのアドレス」をリストにして、
# そこからのリクエストだけを受け付けるようにするものです。
# "https://" + os.environ['WEBSITE_HOSTNAME']は、
# その信頼できるウェブサイトが何かを指定しているんです。
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]

# プログラムのデバッグモードをオフにするという設定
# 本番環境（実際に人が使う状態）では危険なので、Falseにする
DEBUG = False
# SECRET_KEYは、ウェブサイトの秘密の鍵のようなもの
# os.environ['MY_SECRET_KEY']は、この大事な秘密の鍵を、
# サーバーやコンピュータの中に安全に保存されている「環境変数」から読み込んでいます。
SECRET_KEY = os.environ['MY_SECRET_KEY']

# 「ミドルウェア」は、ウェブサイトのリクエストを受け取って、
# 色々な処理をしてくれる手助け役みたいなものです。
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'https://agreeable-mud-00cbb0203.5.azurestaticapps.net'
]

# ウェブサイトで使うファイルがどこに保存されるかを指定する設定
STORAGES = {
    "default": {
        # ファイルをサーバーのファイルシステム（コンピュータのフォルダやファイルの仕組み）に保存することを意味
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        # ファイルをWhiteNoiseという仕組みを使って、圧縮された状態で保存することを意味
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# 「環境変数」という場所から、Azureにあるデータベースに接続するための情報を取り出す
# os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']は、
# Azureのデータベースに接続するための特別な文字列（接続文字列）を取得
CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# 最初に取り出した接続文字列を「辞書」という形に変えるためのコード
# 例：　"host=myserver port=5432 user=admin password=secret"
# CONNECTION.split(' '): 空白で区切って「ペア」（組み合わせ）に分ける
# その後、それぞれのペアを「=」でさらに分ける
# for pair in ...: この分けた情報を辞書という形でまとめる
CONNECTION_STR =  {pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}

# Djangoがどのデータベースを使うかを教える場所
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # 前に作ったCONNECTION_STRという辞書から、
        # dbnameという情報を取り出してデータベースの名前として使っています。
        "NAME": CONNECTION_STR['dbname'],
        # CONNECTION_STRからデータベースのサーバーの場所を指定しています。
        "HOST": CONNECTION_STR['host'],  
        # CONNECTION_STR['user']で、接続するためのユーザー名が指定されています。
        "USER": CONNECTION_STR['user'],
        # CONNECTION_STR['password']で、データベースのパスワードが設定されています。
        "PASSWORD": CONNECTION_STR['password'],
    }
}

# Django（ジャンゴ）というウェブサイトのプログラムが使う静的ファイルをどこに保存するかを指定
# BASE_DIRは、プロジェクトの一番上のフォルダ（つまり、プログラムが保存されている一番大きなフォルダ）の場所
# BASE_DIR/'staticfiles'は、その大きなフォルダの中にある**"staticfiles"**という名前のフォルダを指しています
# つまり、「静的ファイルを全部このフォルダに保存してください」という指定
STATIC_ROOT = BASE_DIR/'staticfiles'