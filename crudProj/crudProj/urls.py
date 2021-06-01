from django.contrib import admin
from django.urls import path
import crudApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudApp.views.main, name='main'),
    #detail페이지로 이동, id를 받아와서 각자만 보여줌
    path('detail/<str:id>/', crudApp.views.detail, name='detail'),
    #read 페이지로 이동.
    path('read/', crudApp.views.read, name = 'read'),
    #create페이지로 이동
    path('new/create/', crudApp.views.create, name='create'),
    #edit 페이지로 이동, id를 받아와서 각자만 보여줌
    path('edit/<str:id>/', crudApp.views.edit, name='edit'),
    #delete 페이지로 이동, id를 받아와서 각자만 보여줌.
    path('delete/<str:id>/', crudApp.views.delete, name='delete'),
]
