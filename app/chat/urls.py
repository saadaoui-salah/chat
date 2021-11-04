from django.urls import path
from .views import peer1, peer11, peer, singup, home, ulogout , peer12 

urlpatterns = [
    path('', peer, name='peer'),
    path('<int:id>', peer11, name='peer11'),
    # path('tmpy/<int:id>', peer12, name='peer12'),
    path('tmpy/', peer12, name='peer12'),
    path('singup', singup, name='singup'),
    path('home', home, name='home'),
    path('logout', ulogout, name='logout'),
#     path('peer1/', peer, name='peer'),
#     path('peer2/', peer, name='peer'),
]