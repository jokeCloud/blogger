from django.urls import path

from .views import PostBusca, PostCategoria, PostDetalhes, PostIndex

urlpatterns = [
    path('', PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>',
         PostCategoria.as_view(), name='post_categoria'),
    path('busca/', PostBusca.as_view(), name='post_busca'),
    path('post/<int:pk>', PostDetalhes.as_view(), name='post_detalhes'),
]
