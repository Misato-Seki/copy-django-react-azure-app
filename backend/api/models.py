# models.py
# 「データの設計図」を作る場所

from django.db import models

# models.Modelは「データの設計図」を作るためのテンプレートみたいなもの
# models.Modelを使うと、Djangoがデータを自動的に整理してくれる

# プロジェクトを管理する人たちのリストを作る
class ProjectManager(models.Model):
    name = models.CharField(unique=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    # models.CharField は「文字を入れるための箱」
    # models.DateField は「日付を入れるための箱」
    # models.DateTimeField は「日付と時間を入れるための箱」
    name = models.CharField(unique=True, max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # ForeignKeyは「つながり」を作るためのもの
    # 「このプロジェクトは、どのプロジェクトマネージャーが担当しているのか」を記録する
    # on_delete=models.CASCADE
    # もしプロジェクトマネージャーが削除されたら、その人が管理しているプロジェクトも一緒に削除される
    projectManager = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
