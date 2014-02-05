from django.conf.urls import patterns, url

urlpatterns = patterns('sbadmin.views',
    url(r'^$','index', name = 'index'),
    url(r'^clientes/$','consultarCli', name = 'consultarCli'),
    url(r'^cliente/$','actualizar', name = 'actualizar'),
    url(r'^servicios/$','consultarSer', name = 'consultarSer'),
    url(r'^servicios/new$','nuevoser', name = 'nuevoser'),
    url(r'^servicios/detail$','detailSer', name = 'detailSer'),
    url(r'^login/$','login', name = 'login'),

)

