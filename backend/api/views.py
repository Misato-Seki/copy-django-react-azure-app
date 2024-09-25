# view.py
# たとえば、誰かが「https://example.com/home」というURLにアクセスしたとする
# そのとき、Djangoは「どのページを見せるか」を views.py の中に探しに行く


# Djangoが提供する便利な機能を使うための準備。
# これで、HTMLファイル（ウェブページのデザイン）を使って返事を作ることができる。
from django.shortcuts import render
# ウェブページで「文字だけの返事」を作るためのもの
from django.http import HttpResponse
# APIを作るための準備
from rest_framework import viewsets, permissions
from .serializers import *
# APIがデータを返すときの返事を作るためのもの
from rest_framework.response import Response
from .models import *

# ホームページを作るための関数
# ユーザーがホームページにアクセスしたときに、"This is the homepage." という
# メッセージを画面に表示するだけの簡単な機能
def home(request):
    return HttpResponse("This is the homepage.")

# このクラスは、プロジェクトの情報を管理するための「API」を作る部分
class ProjectManagerViewset(viewsets.ViewSet):
    # 「誰でもこのAPIにアクセスできるよ」という意味
    permission_classes = [permissions.AllowAny]
    # Projectというデータを全部取り出して使う準備
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer

    # プロジェクトの一覧を見せるための関数
    def list(self, request):
        queryset = ProjectManager.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class ProjectViewset(viewsets.ViewSet):
    # 「誰でもこのAPIにアクセスできるよ」という意味
    permission_classes = [permissions.AllowAny]
    # Projectというデータを全部取り出して使う準備
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # プロジェクトの一覧を見せるための関数
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    # 新しいプロジェクトを作るための関数
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    # 特定のプロジェクトを1つ取り出して見せるための関数
    # pkというのは「プロジェクトのID」のこと
    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    # プロジェクトの情報を変更するための関数
    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    # プロジェクトを削除するための関数
    def destroy(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)
