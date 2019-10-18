from django.db import models

# Create your models here.

#優先順位の欄で使用する選択肢を作成。タプル型。前はオブジェクト名で後ろは表示名。
PRIORITY = (('danger','high'),('info','normal'),('success','low'))

#データの型のクラスTodoModelを作成
class TodoModel(models.Model):
    #CharFieldは字数制限のある文字列。タイトルなどに使う
    title = models.CharField(max_length=100)
    #TextFieldは字数制限なしの文字列。
    memo = models.TextField()
    #優先順位の欄を作成
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY  #choicesはリスト選択型
    )
    #締め切り日欄の作成
    duedate = models.DateField()

    #オブジェクトを文字列で返す_str_メソッドの定義
    #オブジェクトのtitleを文字列で返す
    def __str__(self):
        return self.title