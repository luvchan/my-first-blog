from django.conf import settings
from django.db import models
from django.utils import timezone

# 以下がモデル（オブジェクトとなる）
# クラス名は先頭大文字で定義
# models.ModelはポストがDjango Modelだという意味
# つまりDjangoで扱うオブジェクトなのでDB保存ということになる
class Post(models.Model):
    # それぞれフィールド(本来セルを意味するがドキュメントではカラムとされていた)のタイプを指定する
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #メソッド名は小文字とアンダースコアで記述
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # ダブルアンダースコアでダンダーと呼ぶ,特殊メソッドを意味する
    # 例えば__init__はオブジェクト呼び出し時に自動実行（コンストラクタ）
    # __str__はprint時に自動実行される
    def __str__(self):
        return self.title
