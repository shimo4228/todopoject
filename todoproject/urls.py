from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),

    #''にすることで何もurlを支持しなくてもtodoアプリを呼び出せる
    path('', include('todo.urls')) 
]
