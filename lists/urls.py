from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^lists/(\d+)/$','lists.views.view_list',name='view_list'),
     url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
