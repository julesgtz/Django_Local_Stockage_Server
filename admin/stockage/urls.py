from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_rq),
    path('register/', views.register_rq),
    path('logout/', views.logout_rq),
    path('stockage/', views.stockage),
    path('add/', views.add),
    path('delete/<str:path>', views.delete)
]
