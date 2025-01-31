from django.urls import path
from api.views import UserView, TokenView, ChatView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('login/', TokenView.as_view(), name='login'),
    path('chat/', ChatView.as_view(), name='chat' )
]