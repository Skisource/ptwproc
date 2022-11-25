from django.urls import path
from . import views


app_name = 'ptw'
urlpatterns = [
    # ex: /ptw/smth/
    path('', views.IndexView.as_view(), name='home'),
    path('ptw/', views.PTWView.as_view(), name='ptw_index'),
    path('isolation/', views.IsolationActiveView.as_view(), name='active_index'),
    # path('isolation_longterm/', views.IsolationLongtermView.as_view(), name='longterm_index'),
    path('safe_entry/', views.SafeEntryView.as_view(), name='safe_entry'),
    path('inhibit/', views.InhibitView.as_view(), name='inhibit'),
    # ex: /ptw/5
    path('ptw/<int:ptw_id>/', views.permit, name='detail'),
]
