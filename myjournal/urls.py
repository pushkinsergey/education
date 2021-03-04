
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from Cars.views import index
"""
from Cars.views import addcar
from Cars.views import deletecar
from Cars.views import viewcar
from Cars.views import addjournal
from Cars.views import deletejournal
from Cars.views import viewjournal




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/',LogoutView.as_view(next_page='Cars:index'), name='logout'),
    path('', index),
    path('addcar/', addcar, name='addcar'),
    path('deletecar/<int:idcar>', deletecar, name='deletecar'),
    path('viewcar/<int:idcar>', viewcar, name='viewcar'),
    path('addjournal/<int:idcar>', addjournal, name='addjournal'),
    path('deletejournal/<int:identry>', deletejournal, name='deletejournal'),
    path('viewjournal/<int:identry>', viewjournal, name='viewjournal'),

]
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/',LogoutView.as_view(next_page='Cars:index'), name='logout'),
    path('', index),
    ]