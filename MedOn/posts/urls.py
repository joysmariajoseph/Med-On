from django.conf.urls import url
from django.contrib import admin
#from posts import views

from .views import(
post_create,
post_list,
post_update,
post_detail,
post_delete,

)


urlpatterns = [
    url(r'^/$', posts.views.post_list),

    url(r'^create/$', posts.views.post_create),
    url(r'^detail/(?P<id>\d+)$', posts.views.post_detail),
    url(r'^update/$', posts.views.post_update),
    url(r'^delete/$', posts.views.post_delete),

]
