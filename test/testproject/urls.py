from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url('list_of_users', views.UsersListView.as_view(), name='list_of_users'),
    url('list_of_groups', views.GroupsListView.as_view(), name='list_of_groups'),
    url(r'^users/create/$', views.create_user, name='create_user'),
    url(r'^users/(?P<pk>\d+)/delete/$', views.UsersDelete.as_view(), name='user_delete'),
    url(r'^groups/create/$', views.GroupsCreate.as_view(), name='group_create'),
    url(r'^groups/(?P<pk>\d+)/update/$', views.GroupsUpdate.as_view(), name='group_update'),
    url(r'^groups/(?P<pk>\d+)/delete/$', views.delete_group, name='delete_group'),
    url(r'^user/(?P<pk>[-\w]+)/update/$', views.update_user, name='update_user'),
]