from django.shortcuts import render
#djangoにビルトインのビューをインポート
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
#models.pyからデータの型TodoModelをインポート
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
# ListViewのクラスの作成
class TodoList(ListView):
    # htmlファイルの指定
    template_name = 'list.html'
    # データの型をTodoModelに指定
    model = TodoModel

# DetailViewのクラスの作成
# ListViewとDetailViewの違いは前者がざっくり、後者が細かく表示
class TodoDetail(DetailView):
    # htmlファイルの指定
    template_name = 'detail.html'
    # データの型をTodoModelに指定
    model = TodoModel

# CreateViewのクラスの作成
class TodoCreate(CreateView):
    template_name = 'create.html'
    # データの型をTodoModelに指定
    model = TodoModel
    # 作成するフィールドの指定。TodoModel内のフィールドから選ぶ。
    fields = ('title', 'memo', 'priority', 'duedate')
    # データの作成が成功したときに遷移するＵＲＬの指定。
    # reverse_lazyでlistのＵＲＬを指定
    success_url = reverse_lazy('list')

# DeleteViewのクラスの作成
class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

# UpdateViewクラスの作成
class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')