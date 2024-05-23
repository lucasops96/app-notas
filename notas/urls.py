from django.urls import path
from notas import views

app_name='notas'

urlpatterns = [
    path('',views.listar_notas_user,name='listar_notas_user'),
    path('criar-nota/',views.create_nota,name='create_nota'),
    path('editar-nota/<int:pk>',views.update_nota,name='update_nota'),
    path('excluir-nota/<int:pk>',views.delete_nota,name='delete_nota')
]