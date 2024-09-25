# admin.py
# Djangoの管理サイトに関する設定を行うためのファイル

from django.contrib import admin
from .models import *

# 「プロジェクト」というデータモデルをDjangoの管理サイトに登録するための命令
# 管理サイトの画面で「プロジェクト」のデータを表示したり、
# 編集したりすることができるようになる
admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(TestModel)