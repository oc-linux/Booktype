from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # front page                       
    url(r'^$', 'booki.editor.views.view_frontpage', name="frontpage"),

    # this is temp
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_DOC_ROOT}),

    # debug
    (r'^debug/redis/$', 'booki.editor.views.debug_redis'),                       

    # user accounts                     
    url(r'^accounts/', include('booki.account.urls')),                    

    # groups
    url(r'^groups/(?P<groupid>[\w\s\_\.\-]+)/join/$', 'booki.editor.views.join_group'),                    
    url(r'^groups/(?P<groupid>[\w\s\_\.\-]+)/remove/$', 'booki.editor.views.remove_group'),                    
    url(r'^groups/(?P<groupid>[\w\s\_\.\-]+)/add_book/$', 'booki.editor.views.add_book'),                    
    url(r'^groups/(?P<groupid>[\w\s\_\.\-]+)/remove_book/$', 'booki.editor.views.remove_book'),                    

    url(r'^groups/(?P<groupid>[\w\s\_\.\-]+)/$', 'booki.editor.views.view_group', name="view_group"),                    

    # export
    url(r'^export/(?P<bookid>[\w\s\_\.\-]+)/export/{0,1}$',  'booki.editor.views.view_export', name='export_booki'), 
                       
    # sputnik dispatcher                       
    url(r'^sputnik/$', 'sputnik.views.dispatcher', {
            "map": (  
                (r'^/booki/$',                      'booki.channels.main'),
                (r'^/booki/book/(?P<bookid>\d+)/$', 'booki.channels.editor'),
                (r'^/chat/(?P<bookid>\d+)/$',       'booki.channels.chat')
                )
            }),                     
                       
    # reader
    url(r'^(?P<bookid>[\w\s\_\.\-]+)/', include('booki.editor.urls')),
)
