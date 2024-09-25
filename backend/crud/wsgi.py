"""
WSGI config for crud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# WSGI（ウィスギ）は、「Web Server Gateway Interface」の略です。
# これは、ウェブアプリケーションとウェブサーバーが話すための「ルール」や「橋」のようなものです。

import os

from django.core.wsgi import get_wsgi_application

# os.environは、コンピュータやサーバーの「環境変数」という特別な情報を読み取るためのもの
# WEBSITE_HOSTNAMEは、特定の環境変数の名前
# if 'WEBSITE_HOSTNAME' in os.environ　「もしWEBSITE_HOSTNAMEという環境変数が存在するなら」
setting_module = 'crud.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'crud.settings'

# もしDJANGO_SETTINGS_MODULEという環境変数がまだ設定されていなければ、
# setting_moduleで指定した設定ファイルを使うように設定してください
os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting_module)

application = get_wsgi_application()
 