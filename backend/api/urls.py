# urls.py
# urls.py には、URLと、それに対応するビュー（機能）がセットで書かれている
# このファイルでは、「どのURLでAPIを使えるか」を教えてあげる

# URLを設定するための準備をしている
# でも、実際に使うのは後で出てくる DefaultRouter
from django.urls import path
# 同じフォルダにある views.py から、すべてのビュー（機能）を持ってきている
# たとえば、ProjectViewset というAPIの機能もここに含まれている
from .views import *
# DefaultRouterは、APIのための「URLの地図」を自動で作ってくれるツール
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 'project': APIのURLの一部として「project」という名前を使う
# ProjectViewset: このAPIの機能を作る「ビューセット」を指定
# 「project」というURLがアクセスされたときに、この機能を使うことができる
# APIの名前をわかりやすくするためのもの
router.register('project', ProjectViewset, basename='project')
router.register('projectManager', ProjectManagerViewset, basename='projectManager')
# router が作った「APIの地図」を urlpatterns にセット
# DjangoはどのURLでどの機能を使うかを自動でわかるようになる
urlpatterns = router.urls


# urlpatterns = [
#     path('', home)
# ]