# シリアライザーは、データを「わかりやすい形」に変換するのに使う
# たとえば、データベースから取ったデータを、JSONという形式に変換してウェブページに表示
from rest_framework import serializers
from .models import *

# serializers.ModelSerializer: これは、データを簡単に変換するための「基本的なツール」のこと。
# これを使うと、モデル（データの設計図）をもとに、データの形を自動で作ることができる
class ProjectSerializer(serializers.ModelSerializer):
    # class Meta は、シリアライザーやモデルの「設定をまとめるための特別なクラス」
    class Meta:
        # ここでは、Project というデータのテンプレートを使う
        model = Project
        # どのデータを「見せる」または「受け取る」かを指定
        fields = ('id', 'name', 'start_date', 'end_date', 'comments', 'status', 'projectManager')


class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = ('name', 'id')