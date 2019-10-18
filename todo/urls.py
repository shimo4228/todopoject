from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    #as_view()メソッドを使うことでviewオブジェクトを生成
    path('list/', TodoList.as_view(), name = 'list'), 
    #as_view()メソッドを使うことでDetailオブジェクトを生成
    #intはintegerの略なので整数を意味する
    #pkはprimarykeyの略。
    path ('detail/<int:pk>', TodoDetail.as_view(), name = 'detail'),  
    #as_view()メソッドを使うことでCreateオブジェクトを生成
    path('create/' ,TodoCreate.as_view(), name = 'create'),
    #as_view()メソッドを使うことでDeleteオブジェクトを生成
    path('delete/<int:pk>', TodoDelete.as_view(), name = 'delete'),
     #as_view()メソッドを使うことでupdateオブジェクトを生成
    path('update/<int:pk>', TodoUpdate.as_view(), name = 'update')
    ]
